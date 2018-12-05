

values = {
            'date_time'   : 'self.date_time_string()',
            'client_host' : 'self.client_address[0]',
            'client_port' : 'self.client_address[1]',
            'command'     : 'self.command',
            'path'        : 'self.path'
        }


def func(**args):
    print(type(args)) # dict
    for k,v in args.items():
        print(k, v, sep=':')


# ** 将 values 解包 
#func(**values)

import time
print("""<table>
        <tr>  <td>Header</td>         <td>Value</td>          </tr>
        <tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
        <tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
        <tr>  <td>Client port</td>    <td>{client_port}s</td> </tr>
        <tr>  <td>Command</td>        <td>{command}</td>      </tr>
        <tr>  <td>Path</td>           <td>{path}</td>         </tr>
        </table>""".format(date_time=time.ctime(),client_host="localhost",
                           client_port='8080', command="notepad",
                           path="/home/xuef"))






