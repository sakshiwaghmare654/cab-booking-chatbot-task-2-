import random

while True:
  print('\n=== CAB BOOKING CHATBOT ===')
  print('1. Book Ride')
  print('2. Exit')

  choice = input('Enter your choice (1 or 2): ')

  if choice == '1':
    # Cab Selection
    print('\nSelect Cab Type:')
    print('1. Auto - Rs 12/km')
    print('2. Sedan - Rs 18/km')
    print('3. SUV - Rs 25/km')

    cab_choice = input('Enter cab choice (1-3): ')

    if cab_choice == '1':
      cab_type = 'Auto'
      rate = 12
    elif cab_choice == '2':
      cab_type = 'Sedan'
      rate = 18
    elif cab_choice == '3':
      cab_type = 'SUV'
      rate = 25
    else:
      print('Invalid cab choice! Please try again.')
      continue

    # Route Selection
    print('\nSelect Route:')
    print('1. Pune Station to Shivajinagar (5 km)')
    print('2. Swargate to Kothrud (8 km)')
    print('3. Hinjawadi to Wakad (10 km)')

    route_choice = input('Enter route choice (1-3): ')

    if route_choice == '1':
      source = 'Pune Station'
      dest = 'Shivajinagar'
      dist = 5
    elif route_choice == '2':
      source = 'Swargate'
      dest = 'Kothrud'
      dist = 8
    elif route_choice == '3':
      source = 'Hinjawadi'
      dest = 'Wakad'
      dist = 10
    else:
      print('Invalid route choice! Please try again.')
      continue

    # Fare Calculation
    total_fare = dist * rate

    print('\n--- Ride Summary ---')
    print('Cab Type:', cab_type)
    print('Route:', source, 'to', dest)
    print('Distance:', dist, 'km')
    print('Rate per km: Rs', rate)
    print('Total Fare: Rs', total_fare)

    # Confirmation & OTP Cancellation rule
    print('\nConfirm Booking?')
    print('1. Confirm & Share OTP')
    print('2. Cancel Ride')

    confirm = input('Enter choice (1 or 2): ')

    if confirm == '1':
      # 4 digit OTP generation
      otp = random.randint(1000, 9999)
      print('\nBooking Confirmed!')
      print('Your 4-digit OTP is:', otp)
      print(
          'Note: Once OTP is shared, ride cannot be cancelled as per rules.'
      )
    elif confirm == '2':
      print('\nRide cancelled successfully!')
    else:
      print('Invalid choice, returning to main menu.')

  elif choice == '2':
    print('Thank you for using Cab Booking Chatbot! Goodbye.')
    break

  else:
    print('Invalid choice! Please select 1 or 2.')