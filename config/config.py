login_pages = {
    "lpadmin": "inurl:admin",
    "lplogin": "inurl:login",
    "lpadminlogin": "inurl:adminlogin",
    "lpcplogin": "inurl:cplogin",
    "lpweblogin": "inurl:weblogin",
    "lpquicklogin": "inurl:quicklogin",
    "lpwp1": "inurl:wp-admin",
    "lpwp2": "inurl:wp-login",
    "lpportal": "inurl:portal",
    "lpuserportal": "inurl:userportal",
    "lploginpanel": "inurl:loginpanel",
    "lpmemberlogin": "inurl:memberlogin",
    "lpremote": "inurl:remote",
    "lpdashboard": "inurl:dashboard",
    "lpauth": "inurl:auth",
    "lpexc": "inurl:exchange",
    "lpfp": "inurl:ForgotPassword",
    "lptest": "inurl:test",
    "lpgit": "inurl:.git",
    "lpbkp": "inurl:backup"
}

file_types = {
    "ftdoc": "filetype:doc",
    "ftdot": "filetype:dot",
    "ftdocm": "filetype:docm",
    "ftdocx": "filetype:docx",
    "ftdotx": "filetype:dotx",
    "ftxls": "filetype:xls",
    "ftxlsm": "filetype:xlsm",
    "ftxlsx": "filetype:xlsx",
    "ftppt": "filetype:ppt",
    "ftpptx": "filetype:pptx",
    "ftmdb": "filetype:mdb",
    "ftpdf": "filetype:pdf",
    "ftsql": "filetype:sql",
    "fttxt": "filetype:txt",
    "ftrtf": "filetype:rtf",
    "ftcsv": "filetype:csv",
    "ftxml": "filetype:xml",
    "ftconf": "filetype:conf",
    "ftdat": "filetype:dat",
    "ftini": "filetype:ini",
    "ftlog": "filetype:log",
    "ftidrsa": "index%20of:id_rsa%20id_rsa.pub",
    "ftpy": "filetype:py",
    "ftphtml": "filetype:html",
    "ftpsh": "filetype:sh",
    "ftpodt": "filetype:odt",
    "ftpkey": "filetype:key",
    "ftpsgn": "filetype:sign",
    "ftpmd": "filetype:md",
    "ftpold": "filetype:old",
    "ftpbin": "filetype:bin",
    "ftcer": "filetype:cer",
    "ftcrt": "filetype:crt",
    "ftpfx": "filetype:pfx",
    "ftcrl": "filetype:crl",
    "ftcrs": "filetype:crs",
    "ftder": "filetype:der",
    "ftappages": "filetype:pages",
    "ftappresent": "filetype:keynote",
    "ftappnumbers": "filetype:numbers",
    "ftodt": "filetype:odt",
    "ftods": "filetype:ods",
    "ftodp": "filetype:odp",
    "ftodg": "filetype:odg"
}

dir_traversal = {
    "dtparent": 'intitle:%22index%20of%22%20%22parent%20directory%22',  # Common traversal
    "dtdcim": 'intitle:%22index%20of%22%20%22DCIM%22',  # Photo
    "dtftp": 'intitle:%22index%20of%22%20%22ftp%22',  # FTP
    "dtbackup": 'intitle:%22index%20of%22%20%22backup%22',  # BackUp
    "dtmail": 'intitle:%22index%20of%22%20%22mail%22',  # Mail
    "dtpassword": 'intitle:%22index%20of%22%20%22password%22',  # Password
    "dtpub": 'intitle:%22index%20of%22%20%22pub%22',  # Pub
    "dtgit": 'intitle:%22index%20of%22%20%22.git%22',  # Git
    "dtlog": 'intitle:%22index%20of%22%20%22log%22',  # Log - Log files
    "dtconf": 'intitle:%22index%20of%22%20%22src%22',  # Src - Sourcecodes
    "dtenv": 'intitle:%22index%20of%22%20%22env%22',  # Env - Environment settings
    "dtdenv": 'intitle:%22index%20of%22%20%22.env%22',  # .Env - Environment settings
    "dtdsql": 'intitle:%22index%20of%22%20%22.sql%22',  # .Sql - Sql settings or dbs
    "dtapi": 'intitle:%22index%20of%22%20%22api%22',  # Api - Sensitive info about an API
    "dtvenv": 'intitle:%22index%20of%22%20%22venv%22',  # Virtual Environment Python
    "dtadmin": 'intitle:%22index%20of%22%20%admin%22'  # Admin
}
