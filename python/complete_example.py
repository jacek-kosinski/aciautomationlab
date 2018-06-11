from acitoolkit.acitoolkit import Session, Credentials, Tenant

creds = Credentials('apic', 'Opis co skrypt robi.')
args = creds.get()

session = Session(args.url, args.login, args.password)

resp = session.login()
if not resp.ok:
    print 'Could not login to APIC'

tenant = Tenant('mytenat')

resp = session.push_to_apic(tenant.get_url(), tenant.get_json())
if not resp.ok:
    print 'Could not push configuration to APIC'
    print resp.text

tenants = Tenant.get(session)
for tenant in tenants:
    print tenant.name

session.close()
