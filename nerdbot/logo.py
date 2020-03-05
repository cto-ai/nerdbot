from cto_ai import sdk, ux
cto_terminal = """
      [94m██████[39m[33m╗[39m [94m████████[39m[33m╗[39m  [94m██████[39m[33m╗ [39m      [94m█████[39m[33m╗[39m  [94m██[39m[33m╗[39m
     [94m██[39m[33m╔════╝[39m [33m╚══[39m[94m██[39m[33m╔══╝[39m [94m██[39m[33m╔═══[39m[94m██[39m[33m╗[39m     [94m██[39m[33m╔══[39m[94m██[39m[33m╗[39m [94m██[39m[33m║[39m
     [94m██[39m[33m║     [39m [94m   ██[39m[33m║   [39m [94m██[39m[33m║[39m[94m   ██[39m[33m║[39m     [94m███████[39m[33m║[39m [94m██[39m[33m║[39m
     [94m██[39m[33m║     [39m [94m   ██[39m[33m║   [39m [94m██[39m[33m║[39m[94m   ██[39m[33m║[39m     [94m██[39m[33m╔══[39m[94m██[39m[33m║[39m [94m██[39m[33m║[39m
     [33m╚[39m[94m██████[39m[33m╗[39m [94m   ██[39m[33m║   [39m [33m╚[39m[94m██████[39m[33m╔╝[39m [94m██[39m[33m╗[39m [94m██[39m[33m║[39m[94m  ██[39m[33m║[39m [94m██[39m[33m║[39m
     [33m ╚═════╝[39m [33m   ╚═╝   [39m [33m ╚═════╝ [39m [33m╚═╝[39m [33m╚═╝  ╚═╝[39m [33m╚═╝[39m

 We’re building the world’s best developer experiences.
 """

cto_slack = """:white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square:
:white_square::white_square::black_square::black_square::white_square::white_square::black_square::black_square::black_square::white_square::white_square::white_square::black_square::black_square::black_square::white_square:
:white_square::black_square::white_square::white_square::black_square::white_square::black_square::white_square::white_square::black_square::white_square::black_square::white_square::white_square::white_square::white_square:
:white_square::black_square::white_square::white_square::black_square::white_square::black_square::black_square::black_square::white_square::white_square::white_square::black_square::black_square::white_square::white_square:
:white_square::black_square::white_square::white_square::black_square::white_square::black_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square::black_square::white_square:
:white_square::white_square::black_square::black_square::white_square::white_square::black_square::white_square::white_square::white_square::white_square::black_square::black_square::black_square::white_square::white_square:
:white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square::white_square:"""

def logo_print(): 
    if sdk.get_interface_type() == 'terminal': 
        ux.print(cto_terminal)
    else: 
        ux.print(cto_slack)
