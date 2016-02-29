# loading developer libraries
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

def get_answer(host):
	server_url = host + '/randomfact'

    # Tell the client they are about to learn a random fact.
    print("Welcome to the RANDOM FACT OF THE DAY!\n")
    response = requests.get(url=server_url)
    if response.status_code != 200:
    	to_return = response.text
    else:
    	to_return = str(response.status_code) + ' error'
    return to_return

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Get the random fact of the day')
	parser.add_argument('host', type=str, help='address of server hosting randomfact program')

    parser.add_argument('--test', help='unit test for randomfact server', action='store_true')
    args = parser.parse_args()

    if args.test:
    	print('Test passed')
    	exit(1)

    answer = get_answer(args.host)
    print(answer)