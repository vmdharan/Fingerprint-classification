# Fingerprint.py
# Group fingerprints using the Henry Classification System.

class Fingerprint:
    
    # Process the fingerprint.
    def Henry(self, Fingers):

        # Define the indices for each finger. The numbering system
        # starts from the fingers on the right hand and increases
        # sequentially to the left.
        
        # Left hand - palm faces downwards.
        LPinky = 10
        LRing = 9
        LMiddle = 8
        LIndex = 7
        LThumb = 6

        # Right hand - palm faces upwards.
        RPinky = 5
        RRing = 4
        RMiddle = 3
        RIndex = 2
        RThumb = 1

        # Define the print type, whether it is Arch, Loop or Whorl
        def printType(P):
            # This is a Whorl pattern.
            if(P == 'W'):
                return True
            
            # This is either an Arch or Loop pattern.
            return False

        # Contain the value of even and odd finger patterns.
        EvenFingers = 0
        OddFingers = 0

        # Check for the Whorl pattern in the even numbered fingers.
        if(printType(Fingers[LPinky - 1])):
            EvenFingers += 1
        
        if(printType(Fingers[LMiddle - 1])):
            EvenFingers += 2

        if(printType(Fingers[LThumb - 1])):
            EvenFingers += 4
        
        if(printType(Fingers[RRing - 1])):
            EvenFingers += 8
        
        if(printType(Fingers[RIndex - 1])):
            EvenFingers += 16
        
        # Check for the Whorl pattern in the odd numbered fingers.
        if(printType(Fingers[LRing - 1])):
            OddFingers += 1
        
        if(printType(Fingers[LIndex - 1])):
            OddFingers += 2

        if(printType(Fingers[RPinky - 1])):
            OddFingers += 4
        
        if(printType(Fingers[RMiddle - 1])):
            OddFingers += 8
        
        if(printType(Fingers[RThumb - 1])):
            OddFingers += 16

        # Determine the grouping.
        Grouping = [1+EvenFingers, 1+OddFingers]

        return Grouping
