
a = """
____###_____########______###_____########______###_____########______###_____########__
___###_____###____###____###_____###____###____###_____###____###____###_____###____###_
__###_###________###____###_###________###____###_###________###____###_###________###__
_###__###______###_____###__###______###_____###__###______###_____###__###______###____
###########__###______###########__###______###########__###______###########__###______
______###___###_____________###___###_____________###___###_____________###___###_______
______###__##########_______###__##########_______###__##########_______###__##########e
"""

b = """+++++++++[>+<-]>+.<+++++++++[>++<-]>+++++++..<+++++++++[>++++++<-]>+++.<+++++++++[>------<-]>------...+++..<+++++++++[>++++++<-]>+++.<+++++++++[>------<-]>------..+++......<+++++++++[>++++++<-]>+++.<+++++++++[>------<-]>------..<+++++++++[>--<-]>----.<+++++++++[>++<-]>+++++++..---.<+++++++++[>++++++++++<-]>++.<+++++++++[>----------<-]>--..+++..---.<+++++++++[>++++++++++<-]>++.<+++++++++[>---------<-]>--------..---..<+++++++++[>+++++++<-]>..<+++++++++[>------<-]>------..<+++++++++[>++++++<-]>+++.<+++++++++[>------<-]>------.<+++++++++[>--<-]>----.<+++++++++[>++<-]>+++++++..---.<+++++++++[>++++++++++<-]>++.<+++++++++[>----------<-]>--..+++..---.<+++++++++[>++++++++++<-]>++.<+++++++++[>---<-]>-----.+++..<+++++++++[>-----<-]>---.<+++++++++[>-<-]>------..+++..---.<+++++++++[>++++++++++<-]>++.<+++++++++[>------------<-]>------.<+++++++++[>++<-]>+++++++........---.<+++++++++[>++++++++++<-]>++.<+++++++++[>----------<-]>--.+++......---..<+++++++++[>++++++++++<-]>++.<+++++++++[>------------<-]>------.<+++++++++[>+++++++++<-]>+.+++.....<+++++++++[>------<-]>------..---.<+++++++++[>++++++++++<-]>++.<+++++++++[>---------<-]>--------..---..<+++++++++[>+++++++<-]>....<+++++++++[>-----<-]>---.<+++++++++[>-<-]>------.<+++++++++[>--<-]>----.<+++++++++[>++<-]>++++......+++..---.<+++++++++[>++++++++++<-]>++.<+++++++++[>---------<-]>--------..---.<+++++++++[>++++++++++<-]>++.<+++++++++[>----------<-]>--......<+++++++++[>--<-]>----.<+++++++++[>++<-]>++++......+++..---.<+++++++++[>++++++++++<-]>++.<+++++++++[>---------<-]>--------........<+++++++++[>++++++<-]>+++.<+++++++++[>------<-]>------.<+++++++++[>--<-]>----.<+++++++++[>++<-]>++++......<+++++++++[>++++++<-]>++++++.+++..<+++++++++[>+++<-]>++.<+++++++++[>---<-]>-----.+++........<+++++++++[>+++<-]>++.<+++++++++[>------------<-]>------.."""

o = 0
i = 0
while i <= len(b)-1:
	if a[o] == "_":
		print(" ", end="")
	elif a[o] == "#":
		print(b[i], end="")
		i=i+1
	elif a[o] == "\n":
		print()
	elif a[o] == "e":
		print(" ")
		o = -1
	o = o  +1


