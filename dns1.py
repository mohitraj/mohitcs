# The code is modified By MOHIT
# email mohitraj.cs@gmail.com

from twisted.internet import reactor, defer
from twisted.names import client, dns, error, server
import argparse 
class DNS_Reslover(object):
    def __init__(self, p,ip):
        self._pattern = p
        self._network = ip
   

    def _dynamicResponseRequired(self, query):
        if query.type == dns.A:
            labels = query.name.name.split(b'.')
            #import pdb;pdb.set_trace()
            if labels[0].startswith(self._pattern.encode()):
                return True
        return False

    def _doDynamicResponse(self, query):
        name = query.name.name
        labels = name.split(b'.')
        parts = labels[0].split(self._pattern.encode())
        lastOctet = parts[1]
        address=self._network.encode()+b"."+ lastOctet
        answer = dns.RRHeader(
            name=name,
            payload=dns.Record_A(address))        
        answers = [answer]
        authority = []
        additional = []
        return answers, authority, additional

    def query(self, query, timeout=None):
        if self._dynamicResponseRequired(query):
            return defer.succeed(self._doDynamicResponse(query))
        else:
            return defer.fail(error.DomainError())

def main(pattern,IP):
    factory = server.DNSServerFactory(
        clients=[DNS_Reslover(pattern,IP), client.Resolver(resolv='/etc/resolv.conf')]
    )
    protocol = dns.DNSDatagramProtocol(controller=factory)
    reactor.listenUDP(53, protocol)
    reactor.listenTCP(53, factory)
    reactor.run()
	
def main_arg():
    version1 = 1.0
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', nargs=2, help='First give pattern then IP')
    parser.add_argument('-v', help="Version Number",action='store_const',const=version1 )

    args = parser.parse_args()
    try :
        if args.o and len(args.o)==2:
            pattern, IP= args.o
            main(pattern,IP)

        elif args.v:
            print ("Current Version is ",args.v)
        else :
            print ("Use -h for the options")
        print ("For more help email to mohitraj.cs@gmail.com")
    except Exception as e :
        print (e)

if __name__ == '__main__':
	main_arg()
