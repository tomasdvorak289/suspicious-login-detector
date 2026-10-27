from src.transform import count_failed_logins




def is_suspicious(occured, limit):
      
    """
        vypíše true nebo false podle toho zda počet přihlášení je podezřelý
        
        Args:
        occured : počet kolikrát proběhl nepsoěšný pokus o přihlášení
        limit : počet neúspěšných přihlášení který již považuji za podezřelý
    
        Returns:
        vrací True  / False, podle toho zda je occured větší nebo rovno limit
    """
      
    if occured >= limit:
        return True
    else:
        return False







def find_suspicious_ips(failed_counts, limit=3) : 
    """
    Finds suspicious IP addresses based on failed login attempts.

    Args:
        failed_counts: Dictionary containing IP addresses as keys
            and the number of failed login attempts as values.
        limit: Minimum number of failed attempts required
            to consider an IP address suspicious. Defaults to 3.

    Returns:
        List of IP addresses that have reached or exceeded
        the specified limit.
    """
    suspicious_ips = []
    for k,v in failed_counts.items():
        if is_suspicious(v, limit) == True:
                suspicious_ips.append(k)
    return suspicious_ips





def detect_suspicious_logins(logins_list, limit=3):
    """
    Detects suspicious IP addresses from login records.

    Args:
        logins_list: List of login records containing IP addresses
            and login statuses.
        limit: Minimum number of failed login attempts required
            to mark an IP address as suspicious. Defaults to 3.

    Returns:
        List of IP addresses considered suspicious.

    Raises:
        KeyError: If a required key is missing from a login record.
    """
    failed_counts = count_failed_logins(logins_list)
    suspicious_ips = find_suspicious_ips(failed_counts, limit)
    return(suspicious_ips)

