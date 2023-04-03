
import PySimpleGUI as psg
import qrcode 
import os



layout = [
    [psg.Text('Enter text or link:', background_color = 'teal') ,psg.InputText(key='text')],
    [psg.Text('Specify QR code size:',background_color = 'teal'), psg.Slider(range=(1, 10), orientation='h', default_value=4, key='size')],
    [psg.Text('Specify QR code color:',background_color = 'teal')],
    [psg.Radio('Black', "COLOR", background_color = 'teal', default=True, key='color_black'), psg.Radio('Grey', "COLOR", background_color = 'teal', key='color_grey')],
    [psg.Button('Generate QR Code for your text or link ')],
    [psg.Image(key='image')]
]


window = psg.Window('QR Code Generator', layout, background_color = 'teal')


while True:
    event, values = window.read()
    if event == psg.WINDOW_CLOSED:
        break

    if event == 'Generate QR Code for your text or link ':
        
        qr = qrcode.QRCode(version=2, box_size=values['size'], border=2)
        qr.add_data(values['text'])
        qr.make(fit=True)
        img = qr.make_image(fill_color='black' if values['color_black'] else 'grey', back_color='white')

       
        img_file = 'qrcodg' + '.png'
        path = os.path.join(os.getcwd(),img_file)
        img.save(path)

       
        window['image'].update(filename=path)



window.close()

