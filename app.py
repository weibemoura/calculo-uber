import sys

from crawler.uber import FareEstimate


def confirme_address(label, message, options):
    print(label, '(Press q for exit)')

    for x, address in enumerate(options):
        title = address['title']
        print(f'{x+1}: {title}')

    try:
        opt = input(message)
        if not opt == 'q':
            return options[int(opt) - 1]
    except Exception as ex:
        return confirme_address(label, message, options)

    sys.exit(0)


def main():
    estimate = FareEstimate()
    pickup_options = estimate.get_ref_address('Qr 614 Conjunto 6 7')
    destination_options = estimate.get_ref_address('QNM 23 Conjunto G')

    pickup = confirme_address('Pickup Ref', 'confirme your address: ', pickup_options)
    destination = confirme_address('Pickup Ref', 'confirme your address: ', destination_options)

    prices = estimate.get_prices(pickup, destination)
    for price in prices:
        print(price)


if __name__ == '__main__':
    main()
