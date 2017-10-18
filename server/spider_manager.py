from flask import Flask, url_for, redirect, request, json, session,Response
from flask import render_template
from app.controler.DB_run_contorllar import run_contor
import sys
import re
app = Flask(__name__)
reload(sys)

sys.setdefaultencoding('utf8')


@app.route('/update_status')
#getLP?creativeID=838
def update_status_():
	r=""
	status=""
	des=""
	account_id=""
	# ip_=request.remote_addr
	# UA_=request.headers.get('User-Agent')
	args=request.args.items()
	for x in xrange(0,len(args)):
		if args[x][0].lower()=="status".lower():
			print(args[x][1])
			status=re.sub("[^\w]+","",args[x][1])
		if args[x][0].lower()=="des".lower():
			print(args[x][1])
			des=re.sub("[^\w]+","",args[x][1])
		if args[x][0].lower()=="account_id".lower():
			print(args[x][1])
			account_id=re.sub("[^\w]+","",args[x][1])
	if status!="1" and status!="2" and  status!="0":
		print 1
		r='{"status":"404"}'
	else:
		r=run_contor.update_status(status[0:10],des[0:40],account_id[0:10])
	
	return str(r)
@app.route('/get_userinfo')
def get_userinfo_():
	r=""
	account_id=""
	# ip_=request.remote_addr
	# UA_=request.headers.get('User-Agent')
	args=request.args.items()
	for x in xrange(0,len(args)):
		if args[x][0].lower()=="account_id".lower():
			print(args[x][1])
			account_id=re.sub("[^\w]+","",args[x][1])
	if account_id!='' and account_id is not None:
		r=run_contor.userinfo(account_id[0:10])
	else:
		r='{"status":"404"}'
	return str(r)

@app.route('/import_spend')
def import_spend_():
	r=""
	account_id=""
	account_balance=""
	account_spend_today=""
	# ip_=request.remote_addr
	# UA_=request.headers.get('User-Agent')
	args=request.args.items()
	for x in xrange(0,len(args)):
		if args[x][0].lower()=="account_id".lower():
			print(args[x][1])
			account_id=re.sub("[^0-9.]+","",args[x][1])
		if args[x][0].lower()=="account_balance".lower():
			print(args[x][1])
			account_balance=re.sub("[^0-9.]+","",args[x][1])
		if args[x][0].lower()=="account_spend_today".lower():
			print(args[x][1])
			account_spend_today=re.sub("[^0-9.]+","",args[x][1])
	if account_id!='' and account_id is not None:
		r=run_contor.import_spend(account_id[0:10],account_balance[0:40],account_spend_today[0:40])
	else:
		r='{"status":"404"}'
	return str(r)


@app.route('/update_user_info',methods=['POST'])
def update_user_info_():
	r=""
	account_id=""
	media_id=""
	cookies_=""
	# ip_=request.remote_addr
	# UA_=request.headers.get('User-Agent')

	args=request.args.items()


	for x in xrange(0,len(args)):


		if args[x][0].lower()=="account_id".lower():
			print(args[x][1])
			account_id=re.sub("[^0-9.]+","",args[x][1])
		if args[x][0].lower()=="media_id".lower():
			print(args[x][1])
			media_id=re.sub("[^\w]+","",args[x][1])
		if args[x][0].lower()=="cookies_".lower():
			print(args[x][1])
			cookies_=args[x][1]

	if account_id!='' and account_id is not None:
		r=run_contor.update_user_info(account_id[0:10],media_id,cookies_)
	else:
		r='{"status":"404"}'
	return str(r)

if __name__ == '__main__':

	app.debug = True
	app.run(host='0.0.0.0', port=1110)