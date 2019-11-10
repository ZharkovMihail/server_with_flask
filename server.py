import json
#import redis
from flask import Flask, request, Response, make_response

app = Flask(__name__)

d={}

@app.route('/<key>/', methods=['GET', 'PUT', 'DELETE'])
def requestic(key):
	key=int("{}".format(key))
	#data = json.loads(request.data)
	if request.method == "PUT":
		data = json.loads(request.data)
		#key = data.get("key")
		message = data.get("message")
		if key == None or message == None:
			return Response(status = 400)
		else:
			d_key = d.get(key)
			if d_key == None:
				d.update({key: message})
				return make_response({key: message}, 201)
			else:
				d.update({key: message})
				return Response(status=200)
			# cache = redis.Redis(host='rediska', port=6379)
			# cache.ping()
			# if not cache.exists(key):
			# 	cache.set(key, json.dumps(message))
			# 	return make_response({"key":"value"}, 201)
			# else:
			# 	cache.delete(key)
			# 	cache.set(key, json.dumps(message))
			# 	return Response(status = 200)

	elif request.method == "GET":
		#key = data.get("key")
		d_key = d.get(key)
		if d_key == None:
			return Response(status=404)
		else:
			return make_response({"message": d_key}, 200)
		# cache = redis.Redis(host='rediska', port=6379)
		# cache.ping()
		# if cache.exists(key):
		# 	res = json.loads(cache.get(key))
		# 	return make_response({"message": res}, 200)
		# else:
		# 	return Response(status=400)

	elif request.method == "DELETE":
		#key = data.get("key")
		if key == None:
			return Response(status=400)
		else:
			d_key = d.get(key)
			if d_key == None:
				return Response(status=404)
			else:
				d.pop(key)
				return make_response({"message": d_key}, 204)
		# cache = redis.Redis(host='rediska', port=6379)
		# cache.ping()
		# if key == None:
		# 	return Response(status = 400)
		# else:
		# 	if cache.exists(key):
		# 		res = json.loads(cache.get(key))
		# 		cache.delete(key)
		# 		return make_response({"message": res}, 204)
		# 	else:
		# 		return Response(status=404)

if __name__ == '__main__':
	app.run()