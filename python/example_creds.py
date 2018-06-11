from acitoolkit.acitoolkit import Credentials

creds = Credentials('apic', 'Opis co skrypt robi.')
args = creds.get()

print args.url
