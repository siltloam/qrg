from pathlib import Path
alpha_nums_path = Path(__file__).parent / "../files/alpha_nums.txt"

class QRCode():
    
    def __init__(self, input=None):
        """Constructor for a QR object

        Args:
            input (String): Input of the QR
            alpha_nums (Set): Set of alphanumeric characters for each QR
        """
        self.input = input
        self.error_correction_level = None
        self.encoding_mode = None
        self.version = 4
        with alpha_nums_path.open() as file:
            self.alpha_nums = set([line.rstrip('\n') for line in file])
            self.alpha_nums.add(" ")
        
        #TODO: run functions here to auto-assign attributes for the QR code
       
    def is_numeric(self):
        """Used to determine whether or not an input is numeric

        Returns:
            bool: If numeric or not
        """
        nums = "0123456789"
        for c in self.input:
            if c in nums:
                pass
            else:
                return False
        return True
        
    def is_alphanumeric(self):
        """Used to determine whether or not an input is alphanumeric.
        Specific alphanumeric requirements are found in files/alpha_nums.txt

        Returns:
            bool: If alphanumeric or not
        """
        for c in self.input:
            if c in self.alpha_nums:
                pass
            else:
                return False
        return True
    
    def set_mode(self):
        """Sets the mode for QR codes to be encoded. We check for numeric
        mode after alphanumeric since alphanumeric supersets numeric
        """
        if self.is_alphanumeric() == True:
            self.encoding_mode = 0b0010
        if self.is_numeric() == True:
            self.encoding_mode = 0b0001
        
    def set_error_correction_level(self):
        """Changes the error correction level for the QR generation
        before encoding the data
        """
        error = input("Please select a level of error correction: (L/M/Q/H)")
        match error:
            case "L":
                self.error_correction_level = "L"
            case "M":
                self.error_correction_level = "M"
            case "Q":
                self.error_correction_level = "Q"
            case "H":
                self.error_correction_level = "H"
            case _:
                error = input("Please select a level of error correction: (L/M/Q/H)")
    
    def get_character_count(self):
        """Returns the binary representation of the character
        count of the string input, important for encoding

        Returns:
            0b(int): Binary representation of input length
        """
        character_count = len(self.input)
        # if alphanumeric pad to 9 bits, if numeric pad to 10 bits
        if self.encoding_mode == 0b0010:
            return format(character_count, '09b')
        elif self.encoding_mode == 0b0001:
            return format(character_count, '010b')
        else:
            return None          
            