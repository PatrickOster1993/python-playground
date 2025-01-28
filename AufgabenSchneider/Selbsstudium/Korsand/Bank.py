class Bank:
    name: str = None
    blz: int
    online_banking: bool
    adress: str = None
    swift_code: int

    def __init__(self, name, blz, online_banking, adress, swift_code)
        self.name = name
        self.blz = blz
        self.online_banking =  online_banking
        self.adress = adress
        self.swift_code =  swift_code