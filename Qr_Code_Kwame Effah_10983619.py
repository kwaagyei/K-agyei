import io
import qrcode
from PySimpleGUI import Window, Input, Button, Column, Image, popup, WIN_CLOSED, Combo, Text


class MainWindow(Window):
    def __init__(self) -> None:
        
        self.layout = [
            [Input()],     
            [Button('Create')],  
            [Column([[Image(key='-QR-')]], size=(300, 300), justification='center')],  
            [Text('Fill Color: '), Combo(['Black', 'White', 'Red', 'Green', 'Blue'], key='-FILL-', default_value='Black')], 
            [Text('Background Color: '), Combo(['White', 'Black', 'Purple','Red', 'Green', 'Blue'], key='-BACK-', default_value='White')], 
            [Text('Border Size: '), Combo(['1', '2', '3', '4', '5'], key='-BORDER-', default_value='4')],  
            [Text('Box Size: '), Combo(['5', '6', '7', '8', '9'], key='-BOX-', default_value='7')],  

        ]
        
        super().__init__('QR Code Generator', self.layout)

    def genCode(self, data, fill_color, back_color, border_size, box_size):
        "Generates the QR code with the specified parameters"
        qr = qrcode.QRCode(version=1, box_size=int(box_size), border=int(border_size))
        qr.add_data(data)
        qr.make(fit=True)
        self.img = qr.make_image(fill_color=fill_color, back_color=back_color)

        
        self.img = self.img.resize((300, 300))
        self.img = self.img.convert('RGB')

        
        self.showCode()

    def showCode(self):
        "Displays the generated QR code"
        with io.BytesIO() as buffer:
        
            self.img.save(buffer, format='PNG')
            img_bytes = buffer.getvalue()
            self['-QR-'].update(data=img_bytes)

    def removeCode(self):
        "Removes the QR code from the container"
        self['-QR-'].update(data=b'')


if __name__ == '__main__':
    
    window = MainWindow()
    while True:
        
        event, values = window.read()
        if event == WIN_CLOSED or event == 'Exit':
            
            window.close()
            
            break
        elif values[0]:
            
            window.genCode(values[0], values['-FILL-'], values['-BACK-'], values['-BORDER-'], values['-BOX-'])
        else: 
           
            popup("Error", "Textfield cannot be empty") 
            window.removeCode()
