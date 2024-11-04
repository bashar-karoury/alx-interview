#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
        method that determines if a given data set represents
        a valid UTF-8 encoding
    """

    # Bytes that never appear in UTF-8: 0xC0, 0xC1, 0xF5–0xFF
    # A "continuation byte" (0x80–0xBF) at the start of a character
    # A non-continuation byte (or the string ending) before the end
    # An overlong encoding
    # A 4-byte sequence that decodes to a value greater that U+10FFFF
    idx = 0
    while (idx < len(data)):
        # check start of sequences
        # check for prohibited characters or continuation byted

        # get byte
        byte = data[idx] & 0xFF
        # print(f'byte {byte:#X} at idx {idx}')
        if (
                byte in [0xC0, 0xC1] or
                (byte >= 0xF5 and byte <= 0xFF) or
                (byte >= 0x80 and byte <= 0xBF)):
            # print(f'Incorrect starting byte {byte:#X} at index {idx}')
            return False

        # Code point ↔ UTF-8 conversion
        # Fcp  	    |Lcp	    | Byte 1	| Byte 2    | Byte 3	| Byte 4
        # U+0000	|U+007F	    |0yyyzzzz	|  -        |  -        | -
        # U+|0080	|U+07|FF	|110xxxyy	|10yyzzzz	|  -        | -
        # U+|0800	|U+FFFF	    |1110wwww	|10xxxxyy	|10yyzzzz	| -
        # U+010000	|U+10FFFF	|11110uvv	|10vvwwww	|10xxxxyy	|10yyzzzz

        # get sequence type
        if (byte >> 7 == 0x0):
            # One Byte Sequence
            # print('----One byte Sequence')
            pass
        if (byte >> 5 == 0x6):
            # print('----Two byte Sequence')
            # Two bytes sequence
            # check next byte
            nextByte = data[idx + 1] & 0xFF
            if nextByte < 0x80 or nextByte > 0xC0:
                # should be a continues byte
                # print('Error, should be continues byte ', nextByte)
                return False
            else:
                # skip next byte; already checked
                idx += 1

        if (byte >> 4 == 0x0E):
            # print('----Three byte Sequence')
            # Three bytes sequences
            # get first byte
            # check second byte is a continues byte
            secondByte = data[idx + 1] & 0xFF
            # print(f'Second byte {secondByte:#X}')
            if secondByte < 0x80 or secondByte > 0xC0:
                # should be a continues byte
                # print('Error, should be continues byte ', secondByte)
                return False
            else:
                # check thrid byte
                idx += 1
                thirdByte = data[idx + 1] & 0xFF
                if thirdByte < 0x80 or thirdByte > 0xC0:
                    # should be a continues byte
                    # print('Error, should be continues byte ', thirdByte)
                    return False
                else:
                    # check for overlong encoding
                    wholeData = ((byte & 0x0F) << 12) | (
                        (secondByte & 0x3F) << 6) | (thirdByte & 0x3F)
                    if wholeData < 0x0800:
                        # print('overlong error ', wholeData)
                        return False
                    idx += 1

        if (byte >> 4 == 0x0F):
            # print('----Four byte Sequence')
            # Three bytes sequences
            # get first byte
            # check second byte is a continues byte
            secondByte = data[idx + 1] & 0xFF
            if secondByte < 0x80 or secondByte > 0xC0:
                # should be a continues byte
                # print('Error, should be continues byte ', secondByte)
                return False
            else:
                # check thrid byte
                idx += 1
                thirdByte = data[idx + 1] & 0xFF
                if thirdByte < 0x80 or thirdByte > 0xC0:
                    # should be a continues byte
                    # print('Error, should be continues byte ', thirdByte)
                    return False
                else:
                    # check thrid byte
                    idx += 1
                    fourthByte = data[idx + 1] & 0xFF
                    if fourthByte < 0x80 or fourthByte > 0xC0:
                        # should be a continues byte
                        # print('Error, should be continues byte ', fourthByte)
                        return False
                    else:
                        # check for overlong encoding
                        wholeData = (
                            ((byte & 0x03) << 18) |
                            ((secondByte & 0x3F) << 12) |
                            ((thirdByte & 0x3F) << 6) |
                            (fourthByte & 0x3F))
                        if wholeData < 0x010000:
                            # print('overlong error ', wholeData)
                            return False
                        # check for value greater that U+10FFFF
                        elif (wholeData > 0x10FFFF):
                            # print('out of range error ', wholeData)
                            return False
                        idx += 1
        idx += 1
    return True
