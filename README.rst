Plone - Open Source Content Management
======================================

`Plone`_ is a free and open source content management system built on
top of the Zope application server. Plone can be used for any kind of
website, including blogs, internet sites, webshops and internal
websites. It's also used as a document publishing system and
collaboration tool. Plone features a flexible workflow, extensibility
and good security.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- Plone configurations:
   
   - Installed from upstream source code to /usr/local/share/plone
   - Plone configured as ZeoCluster:
      
      - Better load balancing options.
      - Ability to run scripts against live/development site.
      - Better debugging.
      - Reserve client for administrative access, etc...

   - Configured Plone/Zeo services to bind to localhost, with Apache
     rewriting URLS and proxying to the ZeoCluster
   - /usr/local/bin/plone-add-apachevhost: custom script to add Plone
     sites as Apache VirtualHosts.

- SSL support out of the box.
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2 and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH: username **root**
-  Plone: username **admin**


.. _Plone: http://plone.org
.. _TurnKey Core: http://www.turnkeylinux.org/core
