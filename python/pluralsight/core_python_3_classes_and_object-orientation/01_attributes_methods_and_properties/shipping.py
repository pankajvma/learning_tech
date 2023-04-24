import iso6346

class ShippingContainer:

    next_serial = 1337  # Class attribute

    # @staticmethod
    # def _generate_serial():             # The leading underscore indicates implementation detail, not intended for use outside.
    #     result = ShippingContainer.next_serial  # Accessing class attribute
    #     ShippingContainer.next_serial += 1      # Modifying class attribute
    #     return result
    
    @classmethod
    def _generate_serial(cls):    # The leading underscore indicates implementation detail, not intended for use outside.
        result = cls.next_serial  # Accessing class attribute
        cls.next_serial += 1      # Modifying class attribute
        return result
    

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])
    

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = ShippingContainer._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )

        # Note: Class attributes can be accessed with the self keyword however, it is not recommended because
        # Instance attrributes take precedence over class attrubutes when accessed through 'self', Also
        # Referring class attribute with self while assigning a new value will create a new instance attribute instead of modifying its value.
