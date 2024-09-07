class QRCode():
    
    def __init__(self, input=None):
        """Constructor for a QR object

        Args:
            input (String): Input of the QR
        """
        self.input = input
        
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
        