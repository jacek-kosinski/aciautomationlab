from acitoolkit import Tenant, AppProfile, EPG

tenant = Tenant('mytenat')
app = AppProfile('myapp', tenant)
epg = EPG('myepg', app)

print tenant.get_json()
