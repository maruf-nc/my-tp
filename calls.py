def search_customer(email=None,phone=None,altphone=None,username=None,customerid=None):
    q = '''
    select USERNAME
          from Tableowner.CUSTOMERINFO
          join Tableowner.USERCUSTINFO
          on CUSTOMERINFO.CUSTOMERID = USERCUSTINFO.CUSTID
          join Tableowner.USERINFO
          on USERINFO.USERID = USERCUSTINFO.USERID
          where username not like '%CSR%'
    '''
    qparams = []
    qargs = []

    if username:
        qparams.append("username=?")
        qargs.append(username)

    if email:
        qparams.append("email=?")
        qargs.append(email)

    for num in [phone,altphone]:
        if num:
            qparams.append("phone=?")
            qargs.append(num)
            qparams.append("altphone=?")
            qargs.append(num)
    if len(qargs) < 1:
        raise TypeError("Function expects at least 1 argument")

    qparamstr = " or ".join(qparams)

    if customerid:
        qparamstr += ' and customerid != ?'
        qargs.append(customerid)

    q += qparamstr

    res = execute_query(q,qargs)

    return res