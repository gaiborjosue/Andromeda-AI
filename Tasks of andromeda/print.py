from escpos.connections import getNetworkPrinter


printer = getNetworkPrinter()(host='192.168.1.13', port=9100)

# printer.text("Hola, como te ha ido, soy Alexa(La asistente de voz de Josue)")
# printer.lf()

printer.align('center')
printer.text('This text is center aligned')
printer.align('right')
printer.text('This text is right aligned')