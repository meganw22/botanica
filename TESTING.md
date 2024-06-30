## Manual Testing
Extensive Manual Testing has been completed:

### Nav Bar and Homepage

| Test Expectation | Test Steps | Test Results | Outcome |
| --- | --- | --- | --- |
| Botanica title button is functional | Test link functionality | Home page loaded | |
| Shop all plants button directs user to products.html page | Test link functionality | All products are loaded | |
| Plant care tips button is functional | Plant care tips button clicked | Plant blog is loaded | |
| Favourites buttons are functional | All 3 favourites buttons are clicked | All buttons load the correct webpages | |
| All category links in the categories drop down takes user to related name page: | Bright Light button clicked | Expected website page loaded | |
| | Low light button clicked | Expected website page loaded | |
| | Easy maintenance button clicked | Expected website page loaded | |
| | For the expert plant carers button clicked | Expected website page loaded | |
| | Lowest to highest price button clicked | Expected website page loaded | |
| | Highest to lowest price button clicked | Expected website page loaded | |
| Plant blog button directs to post_list.html | The 'plant blog' button clicked | Expected website page loaded | |
| Search bar | Blank search is attempted | Error message requests 'search items' | |
| | Plants can be searched using easy and scientific name | Full and partial words find the correct search items | |
| Bag Button is functional | Bag button is clicked | Directs user to bag | |
| Profile page | If user not logged in dropdown displays: 1. Message 'No user logged in' 2. Login here | As expected | |
| | If user is logged in dropdown displays: 1. 'View Profile' Option available 2. 'Logout' Option available | As expected | |
| Footer | All social buttons direct user to selected site | All social buttons are functional | |
| Unauthorised users | CAN access all the above without signing in. | As expected | |

### Products

| Action Taken | Expected Result | Actual Result | Outcome |
| --- | --- | --- | --- |
| Filter options available | Light options display plants: 1. All 2. Low 3. Medium 4. Bright | Plants displayed as expected with appropriate filters listed | |
| | Pet friendly options display plants: 1. All 2. Yes 3. No | Plants displayed as expected with appropriate filters listed | |
| | Ease of Care options display plants: 1. All 2. Easy 3. Moderate 4. Difficult | Plants displayed as expected with appropriate filters listed | |
| | Max Price shows options when searching £1 or more | Plants displayed as expected with appropriate filters listed | |
| | Max price does not allow negative searches | Error message displayed | |
| Product price changes for each plant size | Heights are selected and plant prices change | Prices change when heights are selected | |
| Plant height must be chosen | Plant height selected, plant able to add to bag | As expected | |
| | Plant height not selected, error message to 'select height' shows | As expected | |
| Quantity Selector | Quantity cannot be less than 1 item | As expected | |
| | Quantity cannot be more than 99 items | As expected | |
| Add to bag | Correct Quantity of plants are added to bag | As expected | |
| | Correct Plant height is added to bag | As expected | |
| | Correct Plant Name is added to bag | As expected | |
| | Toast message confirmation message displays | As expected | |
| | Toast 'go to bag' link is functional | As expected | |
| Unauthorised users | CAN access all the above without signing in. | As expected | |

### Bag

| Action Taken | Expected Result | Actual Result | Outcome |
| --- | --- | --- | --- |
| Quantity Selector | Quantity cannot be less than 1 item | Alarm message 'value cannot be below 1' present | |
| | Quantity cannot be more than 99 items | Alarm message 'value cannot be more than 99' | |
| | Update button works correctly, and price updates in order summary | As expected | |
| | Confirmation toasts are present for quantity updates | As expected | |
| Remove Plant button | Confirmation toasts are present for plant removal | As expected | |
| Unauthorised Users cannot checkout | 'Go to Checkout' button clicked and unauth user is directed to sign in. | User directed to sign in | |
| Authorised users can proceed to checkout | 'Go to Checkout' button clicked and unauth user is directed to checkout page | Authorised user can proceed to checkout | |
| Authorised users cannot checkout with an empty bag | Error toast message displays and user directed to products.html | As expected | |
| Delivery fee | Delivery fee is present for orders under delivery threshold and added to total price. | As expected | |
| | Delivery fee is NOT present for orders over delivery threshold | As expected | |

### Checkout

| Action Taken | Expected Result | Actual Result | Outcome |
| --- | --- | --- | --- |
| Form boxes with * must be populated before checkout. | User cannot 'Place Order' with incomplete form | All * form boxes requested content before checkout | |
| User can select existing address if available | Existing address is selected | | |
| | New address form is hidden | | |
| | Payment is successful | | |
| User can enter a new address | Existing address is not selected | | |
| | New address form validation is required | | |
| | Payment is successful | | |
| Stripe authentication | 4242 4242 4242 4242 allows successful order | As expected | |
| | 4000 0025 0000 3155 requests authorisation before making payment | As expected | |
| | Rejection of authorised payment returns 'Payment unauthorised' message | As expected | |
| | Confirmation of authorised payment directs user to Order Success Page | As expected | |
| | Invalid card number message displays | As expected | |
| Checkout Success Page | Order number displayed | As expected | |
| | Correct items shown | As expected | |
| | Correct delivery address shown | As expected | |
| | Correct order total displayed | As expected | |
| | Confirmation toast message with correct order number | As expected | |
| | Back to plants button returns to products.html | Directs user back to plants | |

### Plant Blog

| Action Taken | Expected Result | Actual Result | Outcome |
| --- | --- | --- | --- |
| Plant blog posts can be created by Admin user | Admin able to create post | As expected | |
| Blog posts non-admin users cannot create posts. | Create post button not displayed. | As expected | |
| Admin users can delete a blog post | Admin can delete a blog post successfully | As expected | |
| Admin users can edit a blog post | Admin can edit a blog post successfully | As expected | |
| Unauthorised users cannot like posts | Unauthorised users cannot like posts | As expected | |
| Unauthorised users cannot comment | Unauthorised users cannot comment | As expected | |
| Authorised User can like and unlike a post | Authorised User can like and unlike a post | As expected | |
| Authorised User can create a comment | Authorised User can create a comment | As expected | |
| Authorised User can delete their own comments | Authorised User can delete their own comments | As expected | |
| Authorised User CANNOT delete other users comments | Authorised User CANNOT delete other users comments | As expected | |


## Fixed Bugs


## HTML validator

![html-valid](https://github.com/meganw22/botanica/assets/141934888/49e4c9d2-d526-431c-9efd-1f9f9e89eac6)


## CSS Validator

![css-valid](https://github.com/meganw22/botanica/assets/141934888/250f1717-dcbb-4f12-bd09-ced9cc5a9bb5)

