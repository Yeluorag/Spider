# import base64
import random

class ProxyMiddleware(object):
	def process_request(self, request, spider):
		# Set the location of the proxy
		proxy_ip = random.choice(self.user_agent_ip_list)
		request.meta['proxy'] = "117.90.1.130:9000",
		# print '#'*8, 'The Current ip Address is: ', proxy_ip, '#'*8 

		# # Use the following lines if your proxy requires authentication
		# proxy_user_pass = "aes-256-cfb:eJ0JzcJdPNGM"
		# # setup basic authentication for the proxy
		# encoded_user_pass = base64.encodestring(proxy_user_pass)
		# request.headers['Proxy-Authorization'] = 'Basic' + encoded_user_pass
	user_agent_ip_list = [\
		"117.90.1.130:9000",
		"27.19.107.32:8998",
		"113.242.139.225:8998",
		"121.232.145.198:9000",
		"180.169.59.221:8080"
		]

