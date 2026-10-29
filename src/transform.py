
def count_failed_logins(logins_list):
    """
    Vypíše počty neúspěšných přihlášení k daným ip adresám
    
    Args:
    logins_list :  list přihlášení u kterého chceme zjisit kolikrát se dané ip adrese nepovedlo přihlásit

    Returns:
    slovník s ip adresami, a počtem jejich neúspěšných přihlášení
    """
    try:
        result_count_failed_logins = {}
        for ip in logins_list:
            if ip["status"] == "Failed":
                if ip["ip"] in result_count_failed_logins:
                    result_count_failed_logins[ip["ip"]] = result_count_failed_logins[ip["ip"]] + 1
                else:
                    result_count_failed_logins[ip["ip"]] = 1
        return result_count_failed_logins
    except KeyError as e:
        print("Nastala chyba, chybí ", e)
        raise

