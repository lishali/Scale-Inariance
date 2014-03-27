import requests
 
class MapClient:
  BASE_URL = 'http://dev.virtualearth.net/REST/V1/Routes/Driving?o=json'
  def __init__(self, api_key):
    self.api_key = api_key
    self.url = self.BASE_URL + '&key={}'.format(api_key)
 
  def get_distance(self, point_a, point_b):
    try:
      url = self.url
      url += '&wp.0={}'.format('%20'.join(point_a.split()))
      url += '&wp.1={}'.format('%20'.join(point_b.split()))
      response = requests.get(url)
      data = response.json()
      return data['resourceSets'][0]['resources'][0]['travelDistance']
    except Exception:
      pass
 
if __name__ == '__main__':
  client = MapClient(api_key='AjXDakgWGsf-NVH1pOIKY0PStr1RBH50QNHYBRpSLOZeBAa_ancvEGHTW1mVJTmr')
  print client.get_distance('San Francisco', 'Oakland')