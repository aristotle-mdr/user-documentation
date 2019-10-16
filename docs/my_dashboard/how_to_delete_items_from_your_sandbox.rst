How to delete items from your Sandbox
=====================================

1. Once logged into the registry, navigate to your Dashboard.
   
   .. screenshot::
      :server_path: /account/home
      :alt: My Dashboard
      :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}

#. On your Dashboard, go over to your side panel and select "My Sandbox"
   
   .. screenshot::
      :server_path: /account/home
      :alt: My Dashboard side panel
      :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
      :crop_element: nav[id="user_sidebar"]
      :clicker: a[href="/account/sandbox"]
      
#. From here, you'll be able to review your created items that are not assigned to a Workgroup
      
   .. screenshot::
      :server_path: /account/sandbox
      :alt: My Sandbox
      :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
    
#. On the right hand side of the page, you will be able to select to delete items
   
   .. screenshot::
      :server_path: /account/sandbox
      :alt: Delete option
      :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
      :clicker: a[class="btn btn-default delete-button"]
      
#. Once selecting "delete", you will be prompted if you are sure you want to delete the item
   
   .. screenshot::
      :server_path: /account/sandbox
      :alt: Delete option
      :login: {'url': '/login', "username": "alice@aristotle.example.com", "password": "Administrator"}
      :clicker: a[class="btn btn-default delete-button"]
      
      browser.find_element_by_css_selector('a.btn.btn-default.delete-button').click()
    
      import time
      time.sleep(2)
      
If you are sure you want to delete the item select "Ok", or if not then click the "x" in the upper right corner 
of the pop-out modal.
