from pathlib import Path
alpha_nums_path = Path(__file__).parent / "../files/alpha_nums.txt"

class QRCode():
    
    def __init__(self, input=None):
        """Constructor for a QR object

        Args:
            input (String): Input of the QR
        """
        self.input = input
        with alpha_nums_path.open() as file:
            self.alpha_nums = set([line.rstrip('\n') for line in file])
        
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
        for c in self.input:
            if c in self.alpha_nums:
                pass
            else:
                return False
        return True