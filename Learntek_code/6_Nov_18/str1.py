Type "help", "copyright", "credits" or "license" for more information.
>>> date1  = "09-11-2018"
>>>
>>> date1.split("-")
['09', '11', '2018']
>>>
>>>
>>> name = "learn python"
>>>
>>> name.split()
['learn', 'python']
>>>
>>>
>>> name.split("-")
['learn python']
>>>
>>> ip = "192.168.0.1"
>>> ip.split(".")
['192', '168', '0', '1']
>>>
>>> ip.split(".")[3]
'1'
>>> ip.split(".",1)
['192', '168.0.1']
>>>
>>> ip.split(".",2)
['192', '168', '0.1']
>>> ip
'192.168.0.1'
>>>
>>>
>>> ip.rsplit(".",1)
['192.168.0', '1']
>>>
>>> ip.rsplit(".",2)
['192.168', '0', '1']
>>>
>>>
>>>
>>>
>>> date1 = "21/06/2015"
>>> date1.rsplit("/",1)
['21/06', '2015']
>>> date1.rsplit("/",1)[-1]
'2015'
>>>
