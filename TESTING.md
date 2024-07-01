## Manual Testing
Extensive Manual Testing has been completed:

### Nav Bar and Homepage

| Test Expectation | Test Steps | Test Results | Outcome |
| --- | --- | --- | --- |
| Botanica title button is functional | Test link functionality | Home page loaded | Pass |
| Shop all plants button directs user to `All Plants` page | Test link functionality | All Plants and images are loaded | Pass |
| Plant care tips button is functional | Plant care tips button clicked | `The Plant blog` is loaded | Pass |
| Favourites buttons are functional | All 3 favourites buttons are clicked | All buttons load the correct webpages | Pass |
| All category links in the categories drop down takes user to related name page: | Bright Light button clicked | Expected website page loaded | Pass |
| | Low light button clicked | Expected website page loaded | Pass |
| | Easy maintenance button clicked | Expected website page loaded | Pass |
| | For the expert plant carers button clicked | Expected website page loaded | Pass |
| | Lowest to highest price button clicked | Expected website page loaded | Pass |
| | Highest to lowest price button clicked | Expected website page loaded | Pass |
| Plant blog button directs to `The Plant Blog` page | 'The plant blog' button clicked | Expected website page loaded | Pass |
| Search bar | Blank search is attempted | Error message requests 'search items' | Pass |
| | Plants can be searched using easy and scientific name | Full and partial words find the correct search items | Pass |
| Bag Button is functional | Bag button is clicked | Directs user to bag | Pass |
| Profile page | If user not logged in dropdown displays: 1. Message 'No user logged in' 2. 'Click here to login' | As expected | Pass |
| | If user is logged in dropdown displays: 1. 'View Profile' Option available 2. 'Log out' Option available | As expected | Pass |
| Link to Facebook page | Visit our facebook page is clicked | Facebook opens up to the Botanica Business page | Pass | 
| Working Newsletter form  | User can enter email address successfully | Form is submitted (no email is sent) | Pass | 
| Footer | All social buttons direct user to selected site | All social buttons are functional | Pass |
| Unauthorised users | CAN access all the above without signing in. | As expected | Pass |

### Products

| Action Taken | Expected Result | Actual Result | Outcome |
| --- | --- | --- | --- |
| Filter options available | Light options display plants: 1. All 2. Low 3. Medium 4. Bright | Plants displayed as expected with appropriate filters listed | Pass |
| | Pet friendly options display plants: 1. All 2. Yes 3. No | Plants displayed as expected with appropriate filters listed | Pass |
| | Ease of Care options display plants: 1. All 2. Easy 3. Moderate 4. Difficult | Plants displayed as expected with appropriate filters listed | Pass |
| | Max Price shows options when searching £1 or more | Plants displayed as expected with appropriate filters listed | Pass |
| | Max price does not allow negative searches | Error message displayed | Pass |
| Product price changes for each plant size | Heights are selected and plant prices change | Prices change when heights are selected | Pass |
| Plant height must be chosen | Plant height selected, plant able to add to bag | As expected | Pass |
| | Plant height not selected, error message to 'select height' shows | As expected | Pass |
| Quantity Selector | Quantity cannot be less than 1 item | As expected | Pass |
| | Quantity cannot be more than 99 items | As expected | Pass |
| Add to bag | Correct Quantity of plants are added to bag | As expected | Pass |
| | Correct Plant height is added to bag | As expected | Pass |
| | Correct Plant Name is added to bag | As expected | Pass |
| | Toast message confirmation message displays | As expected | Pass |
| | Toast 'go to bag' link is functional | As expected | Pass |
| Unauthorised users | CAN access all the above without signing in. | As expected | Pass |

### Bag

| Action Taken | Expected Result | Actual Result | Outcome |
| --- | --- | --- | --- |
| Quantity Selector | Quantity cannot be less than 1 item | Alarm message 'value cannot be below 1' present | Pass |
| | Quantity cannot be more than 99 items | Alarm message 'value cannot be more than 99' | Pass |
| | Update button works correctly, and price updates in order summary | As expected | Pass |
| | Confirmation toasts are present for quantity updates | As expected | Pass |
| Remove Plant button | Confirmation toasts are present for plant removal | As expected | Pass |
| Unauthorised Users cannot checkout | 'Go to Checkout' button clicked and unauth user is directed to sign in. | User directed to sign in | Pass |
| Authorised users can proceed to checkout | 'Go to Checkout' button clicked and auth user is directed to checkout page | Authorised user can proceed to checkout page | Pass |
| Authorised users cannot checkout with an empty bag | Error toast message displays and user directed to products.html | As expected | |
| Delivery fee | Delivery fee is present for orders under delivery threshold and added to total price. | As expected | Pass |
| | Delivery fee is NOT present for orders over delivery threshold | As expected | Pass |

### Checkout

| Action Taken | Expected Result | Actual Result | Outcome |
| --- | --- | --- | --- |
| Form boxes with * must be populated before checkout. | User cannot 'Place Order' with incomplete form | All * form boxes requested content before checkout | Pass |
| User can select existing address if available | Existing address is selected, New address form is hidden | Payment is successful | Pass |
| User can enter a new address | Existing address is not selected, new address form validation is required | Payment is successful | Pass |
| Stripe authentication | 4242 4242 4242 4242 allows successful order | As expected | Pass |
| | 4000 0025 0000 3155 requests authorisation before making payment | As expected | Pass |
| | Rejection of authorised payment returns 'Payment unauthorised' message | As expected | Pass |
| | Confirmation of authorised payment directs user to Order Success Page | As expected | Pass |
| | Invalid card number message displays | As expected | Pass |
| Checkout Success Page | Order number displayed | As expected | Pass |
| | Correct items shown | As expected | Pass |
| | Correct delivery address shown | As expected | Pass |
| | Correct order total displayed | As expected | Pass |
| | Confirmation toast message with correct order number | As expected | Pass |
| | Back to plants button returns to products.html | Directs user back to plants | Pass |

### Plant Blog

| Action Taken | Expected Result | Actual Result | Outcome |
| --- | --- | --- | --- |
| Plant blog posts can be created by Admin user | Admin able to create post | As expected | Pass |
| Blog posts non-admin users cannot create posts. | Create post button not displayed. | As expected | Pass |
| Admin users can edit a blog post | Admin can edit a blog post successfully | As expected | Pass |
| Admin users can delete a blog post | Admin can delete a blog post successfully | As expected | Pass |
| Unauthorised users cannot like posts | Unauthorised users cannot like posts | As expected | Pass |
| Unauthorised users cannot comment | Unauthorised users cannot comment | As expected | Pass |
| Authorised User can like and unlike a post | Authorised User can like and unlike a post | As expected | Pass |
| Authorised User can create a comment | Authorised User can create a comment | As expected | Pass |
| Authorised User can delete their own comments | Authorised User can delete their own comments | As expected | Pass |
| Authorised User CANNOT delete other users comments | Authorised User CANNOT delete other users comments | As expected | Pass |


## Fixed Bugs
### Quantity Selector 
I found that the quantity selectors could cause some havoc within the Botanica website, so I committed to finding a fix for this bug:

#### 0 items could be added to bag
When testing a 0 quantity addition to the bag, it would successfully add 0 items to the bag and register the quantity number in the order summary:

![Screenshot 2024-06-29 085334](https://github.com/meganw22/botanica/assets/141934888/07303363-c446-470c-acb9-0d7f5e250432)

Navigating to the bag, the item number would show 0 items and would display the price, but the price would not render in the order total.

![Screenshot 2024-06-29 085811](https://github.com/meganw22/botanica/assets/141934888/16d1760f-47a2-49df-86bc-eccb5df30aee)

This would also register in the order summary, allow a 'successful' checkout, and register 0 items in the Django admin order items summary.

![Screenshot 2024-06-29 085923](https://github.com/meganw22/botanica/assets/141934888/00bebbd7-ff86-4d5d-85bc-38c008662750)

#### Millions of items could be added to the bag
On the other end of the scale, unlimited items could be added to the bag successfully.

![Screenshot 2024-06-29 090123](https://github.com/meganw22/botanica/assets/141934888/dccae57c-64b6-4781-8269-f79f0def45fd)

![Screenshot 2024-06-29 090241](https://github.com/meganw22/botanica/assets/141934888/fe3d7c8d-c4ab-44fa-9e2c-1c06d1bea471)

However, the Stripe payment system would throw an error when the order total exceeded £1 million.

![Screenshot 2024-06-29 090258](https://github.com/meganw22/botanica/assets/141934888/ed6c8fa9-281d-4f0c-9615-fd2ddd8942b3)

Understandably so, as I would also be concerned if someone was purposefully buying £1 million worth of plants online. Naturally, this was a bug I needed to fix. I created some lines of JavaScript to restrict the quantity selector to only allow ordering of 1 to 99 items per order item.

This validation removed all errors and allowed the user to buy sensibly.

## HTML validator

![html-valid](https://github.com/meganw22/botanica/assets/141934888/49e4c9d2-d526-431c-9efd-1f9f9e89eac6)


## CSS Validator

![css-valid](https://github.com/meganw22/botanica/assets/141934888/250f1717-dcbb-4f12-bd09-ced9cc5a9bb5)

