# The code is modified By MOHIT
# email mohitraj.cs@gmail.com

from twisted.internet import reactor, defer
from twisted.names import client, dns, error, server
class DNS_Reslover(object):
    _pattern = 'workstation'
    _network = '172.16.2'

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

def main():
    factory = server.DNSServerFactory(
        clients=[DNS_Reslover(), client.Resolver(resolv='/etc/resolv.conf')]
    )
    protocol = dns.DNSDatagramProtocol(controller=factory)
    reactor.listenUDP(53, protocol)
    reactor.listenTCP(53, factory)
    reactor.run()



if __name__ == '__main__':
	main()
