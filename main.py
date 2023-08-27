import requests
import time
import schedule

API_KEY = '(Write your Cloudflare API)'

# Gets the public ip adress for your machine
def get_public_ip():
  services = [
      'https://api64.ipify.org?format=raw', 'https://ipinfo.io/ip',
      'https://icanhazip.com', 'https://myexternalip.com/raw'
  ]

  for service in services:
    try:
      response = requests.get(service)
      if response.status_code == 200:
        ip_data = response.text.strip()
        print(f"successfully retrived the ip adress : {ip_data} ")
        return ip_data
      else:
        print(
            f"Error: Unable to fetch IP from {service} (Status code: {response.status_code})"
        )
    except Exception as e:
      print(f"An error occurred while fetching IP from {service}: {e}")

  print("Unable to retrieve IP from all services")
  return None

# Updates the ip adress in your cloudflare account
def update_ip(new_ip, record_type, record_name, record_id, ZONE_ID):
  headers = {
      'Authorization': f'Bearer {API_KEY}',
      'Content-Type': 'application/json'
  }

  data = {
      'type': record_type,
      'name': record_name, 
      'content': new_ip
  }

  response = requests.put(
      f'https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{record_id}',
      headers=headers,
      json=data)

  if response.status_code == 200:
    print('IP address updated successfully')
  else:
    print('Error updating IP address')


def run():
  new_ip_address = get_public_ip()

  """
  Note:
  To Get the record id for your dns records, run the following command:
	  curl -X GET "https://api.cloudflare.com/client/v4/zones  /(Write your zone id here)/dns_records" \
     -H "Authorization: Bearer (Write your API key here!)"
  """
  
  # List of records to update
  records_to_update = [
      {
          'ZONE_ID': '(your zone id here)',
          'record_id': '(your record id here)',
          'record_type': '(Record type here)',
          'record_name': '(Record name here)'
      },
      {
          'ZONE_ID': '(your zone id here)',
          'record_id': '(your record id here)',
          'record_type': '(Record type here)',
          'record_name': '(Record name here)'
      },
      # Here you can add more records 
  ]


  for record_info in records_to_update:
      Zone_id = record_info['ZONE_ID']
      record_id = record_info['record_id']
      record_type = record_info['record_type']
      record_name = record_info['record_name']

      if new_ip_address:
          update_ip(new_ip_address, record_type, record_name, record_id, Zone_id)
      else:
          print('Failed')


# Schedule the update_records function to run every x minutes
# The interval is adjustable, default is every 5 minute
schedule.every(5).minutes.do(run)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
