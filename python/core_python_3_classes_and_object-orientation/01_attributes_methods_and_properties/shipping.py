class ShippingContainer:

    next_serial = 1337  # Class attribute

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial     # A0ccessing class attribute
        ShippingContainer.next_serial += 1

        # Note: Class attributes can be accessed with the self keyword however, it is not recommended. Because referring class attribute with self can create instance attribute
