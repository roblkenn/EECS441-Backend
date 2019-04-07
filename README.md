# EECS441-Backend

# Requirements
1. Python 3.x

# Download Instructions
Clone the project
```
git clone https://github.com/roblkenn/EECS441-Backend.git
```
Navigate to the directory EECS441-Backend
```
cd EECS441-Backend
```
Dependencies
```
pip install flask
pip install azure-cosmosdb-table
pip install azure-storage-blob
pip install stripe
npm install --save tipsi-stripe
yarn add stripe
```
Running Flask App in Development Mode
```
  python application.py
```

# File Structure
<pre>
.
├── README.md
├── __init__.py
├── __pycache__
│   ├── auth.cpython-36.pyc
│   ├── dataset.cpython-36.pyc
│   ├── market.cpython-36.pyc
│   └── purchase.cpython-36.pyc
├── application.py
├── auth.py
├── config.py
├── database
│   ├── __init__.py
│   ├── __pycache__
│   │   └── __init__.cpython-36.pyc
│   ├── models
│   │   ├── Blob.py
│   │   ├── Datum.py
│   │   ├── Listing.py
│   │   ├── Purchase.py
│   │   ├── User.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── Blob.cpython-36.pyc
│   │       ├── Datum.cpython-36.pyc
│   │       ├── Listing.cpython-36.pyc
│   │       ├── User.cpython-36.pyc
│   │       └── __init__.cpython-36.pyc
│   └── repositories
│       ├── DatumRepository.py
│       ├── ImageRepository.py
│       ├── ListingRepository.py
│       ├── UserRepository.py
│       ├── __init__.py
│       └── __pycache__
│           ├── DatumRepository.cpython-36.pyc
│           ├── ImageRepository.cpython-36.pyc
│           ├── ListingRepository.cpython-36.pyc
│           ├── UserRepository.cpython-36.pyc
│           └── __init__.cpython-36.pyc
├── dataset.py
├── market.py
├── ml.py
├── model.h5
├── model.json
├── node_modules
│   └── tipsi-stripe
│       ├── CHANGELOG.md
│       ├── LICENSE
│       ├── README.md
│       ├── android
│       │   ├── build.gradle
│       │   └── src
│       │       └── main
│       │           ├── AndroidManifest.xml
│       │           ├── java
│       │           │   └── com
│       │           │       └── gettipsi
│       │           │           └── stripe
│       │           │               ├── CreditCardFormOnChangeEvent.java
│       │           │               ├── CustomCardInputReactManager.java
│       │           │               ├── Errors.java
│       │           │               ├── GoogleApiPayFlowImpl.java
│       │           │               ├── OpenBrowserActivity.java
│       │           │               ├── PayFlow.java
│       │           │               ├── RedirectUriReceiver.java
│       │           │               ├── StripeModule.java
│       │           │               ├── StripeReactPackage.java
│       │           │               ├── dialog
│       │           │               │   └── AddCardDialogFragment.java
│       │           │               └── util
│       │           │                   ├── Action.java
│       │           │                   ├── ArgCheck.java
│       │           │                   ├── CardFlipAnimator.java
│       │           │                   ├── Converters.java
│       │           │                   ├── Fun0.java
│       │           │                   ├── InitializationOptions.java
│       │           │                   ├── PayParams.java
│       │           │                   └── Utils.java
│       │           └── res
│       │               ├── animator
│       │               │   ├── card_flip_left_in.xml
│       │               │   ├── card_flip_left_out.xml
│       │               │   ├── card_flip_right_in.xml
│       │               │   └── card_flip_right_out.xml
│       │               ├── drawable
│       │               │   ├── btn_default_holo_dark.xml
│       │               │   ├── card_512.png
│       │               │   ├── edit_text_holo_dark.xml
│       │               │   ├── header_dark.xml
│       │               │   ├── spinner_background_holo_dark.xml
│       │               │   ├── stp_card_form_back.png
│       │               │   └── stp_card_form_front.png
│       │               ├── drawable-hdpi
│       │               │   ├── btn_default_disabled_focused_holo_dark.9.png
│       │               │   ├── btn_default_disabled_holo_dark.9.png
│       │               │   ├── btn_default_focused_holo_dark.9.png
│       │               │   ├── btn_default_normal_holo_dark.9.png
│       │               │   ├── btn_default_pressed_holo_dark.9.png
│       │               │   ├── spinner_default_holo_dark.9.png
│       │               │   ├── spinner_disabled_holo_dark.9.png
│       │               │   ├── spinner_focused_holo_dark.9.png
│       │               │   ├── spinner_pressed_holo_dark.9.png
│       │               │   ├── textfield_activated_holo_dark.9.png
│       │               │   ├── textfield_default_holo_dark.9.png
│       │               │   ├── textfield_disabled_focused_holo_dark.9.png
│       │               │   └── textfield_disabled_holo_dark.9.png
│       │               ├── layout
│       │               │   ├── payment_form_fragment.xml
│       │               │   └── payment_form_fragment_two.xml
│       │               ├── values
│       │               │   ├── colors.xml
│       │               │   ├── dates.xml
│       │               │   ├── dimens.xml
│       │               │   ├── integers.xml
│       │               │   ├── strings.xml
│       │               │   └── styles.xml
│       │               ├── values-fr
│       │               │   └── strings.xml
│       │               └── xml
│       │                   ├── stub_classic.xml
│       │                   └── stub_material.xml
│       ├── ios
│       │   ├── TPSStripe
│       │   │   ├── TPSCardField.h
│       │   │   ├── TPSCardField.m
│       │   │   ├── TPSCardFieldManager.h
│       │   │   ├── TPSCardFieldManager.m
│       │   │   ├── TPSError.h
│       │   │   ├── TPSError.m
│       │   │   ├── TPSStripeManager.h
│       │   │   └── TPSStripeManager.m
│       │   └── TPSStripe.xcodeproj
│       │       └── project.pbxproj
│       ├── package.json
│       ├── scripts
│       │   ├── build-docs.sh
│       │   ├── local-ci.sh
│       │   ├── post-link-android.js
│       │   ├── post-link-ios.rb
│       │   ├── post-link.sh
│       │   └── pre-link.sh
│       ├── src
│       │   ├── Stripe.js
│       │   ├── components
│       │   │   └── PaymentCardTextField.js
│       │   ├── errorCodes.js
│       │   ├── index.js
│       │   └── utils
│       │       ├── __tests__
│       │       │   └── types.test.js
│       │       ├── checkArgs.js
│       │       ├── checkInit.js
│       │       ├── processTheme.js
│       │       └── types.js
│       └── tipsi-stripe.podspec
├── package-lock.json
├── purchase.py
├── read.txt
├── requirements.txt
└── startup.txt

</pre>
## API Endpoints

/dataset
- get : Retrieve data for use in machine learning model training
- post : Add new datum
- delete : Remove datum

/market
- get : Retrieve listing information
- post : Create a new listing
- put : Update an existing listing (Unused and Commented Out)
- delete : Remove a listing

/purchase
- get : Retrieve payment info for user
- post : Create a charge for user
- put : Update payment info for user
- delete : Remove payment info for user

## Reference Material
[Azure Table Storage Documentation](https://docs.microsoft.com/en-us/azure/cosmos-db/table-storage-how-to-use-python)

[Flask Documentation](http://flask.pocoo.org/docs/1.0/#)
