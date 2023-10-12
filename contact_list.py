class ContactList:
    def __init__(self, name, contacts):
        self._name = name
        self._contacts = sorted(contacts, key=lambda x: x['name'])

    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, name):
        self._name = name

    @property
    def get_contacts(self):
        return self._contacts
    
    @get_contacts.setter
    def set_contacts(self, contacts):
        self._contacts = contacts

    def add_contact(self, contact):
        contacts = self.get_contacts
        contacts.append(contact)
        self.set_contacts = sorted(contacts, key=lambda x: x['name'])

    def remove_contact(self, name):
        contacts = [c for c in self.get_contacts if c['name'] != name]
        self.set_contacts = contacts

    def find_shared_contacts(self, other_list):
        shared_contacts = []
        for contact in self.get_contacts:
            if contact in other_list.get_contacts:
                shared_contacts.append(contact)
        return shared_contacts

