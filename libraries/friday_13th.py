from datetime import date


def friday13(start_year, end_year):
    """
    >>> friday13(1999, 2000)
    ['13 Aug 99', '13 Oct 00']
    >>> friday13(2014, 2015)
    ['13 Jun 14', '13 Feb 15', '13 Mar 15', '13 Nov 15']
    >>> friday13(2018, 2018)
    ['13 Apr 18', '13 Jul 18']
    >>> friday13(2019, 2018)
    []
    >>> friday13(2021, 2022)
    ['13 Aug 21', '13 May 22']
    """
    # Get range of years to check
    results = []
    for year in range(start_year, end_year + 1):
        # Get 13 day of each month and check whether it is Friday or not
        for month in range(1, 13):
            maybe_friday = date(year, month, 13)
            if maybe_friday.isoweekday() == 5:
                # If True add to results
                results.append(maybe_friday.strftime("%d %b %y"))
    return results


if __name__ == '__main__':
    import doctest
    doctest.testmod()
