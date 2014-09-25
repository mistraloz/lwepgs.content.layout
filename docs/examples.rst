Page layout examples
====================

Below are some examples for using the pay layouts.

A Simple Page
-------------

*Most* pages only have to fill three slots: the ``title``, ``breadcrumb``
and the ``body``

.. code-block:: xml

  <html xmlns="http://www.w3.org/1999/xhtml"
        xmlns:tal="http://xml.zope.org/namespaces/tal"
        xmlns:metal="http://xml.zope.org/namespaces/metal"
        metal:use-macro="context/@@groupserver_full_layout/page">
    <head>
      <title metal:fill-slot="title">I am a page: Example</title>
    </head>
    <body>
      <ul metal:fill-slot="breadcrumb">
        <li>
          <a href="/" class="icon-alone">
            <span aria-hidden="true" data-icon="&#x2302;"></span>
            <span class="screen-reader-text">Site home page</span>
          </a>
       </li>
      </ul>
      <div id="a-page" metal:fill-slot="body">
        <p>I am a page, honest.</p>
      </div><!--a-page-->
    </body>
  </html>

The rest of the slots will be filled by the defaults.

Using the ``SiteInfo``
----------------------

Because *most* pages have ``gs.content.base.SitePage`` [#page]_ as the base
view-class there is always a ``siteInfo`` available to use in the ``title``
slot and the rest of the page:

.. code-block:: xml

    <head>
      <title metal:fill-slot="title">I am a page: 
        <span tal:replace="view/siteInfo/name">wibble</span></title>
    </head>

The ``tal:replace`` attribute is used because a ``<span>`` element is not
actually allowed to appear within a ``<title>``. A ``<tal:block>`` could
also be used.

Page-Specific Style and JavaScript
----------------------------------

Some pages have some page-specific CSS styling and JavaScript.

.. code-block:: xml

  <html xmlns="http://www.w3.org/1999/xhtml"
        xmlns:tal="http://xml.zope.org/namespaces/tal"
        xmlns:metal="http://xml.zope.org/namespaces/metal"
        metal:use-macro="context/@@groupserver_full_layout/page">
    <head>
      <title metal:fill-slot="title">I am a page: Example</title>
      <style type="text/css" metal:fill-slot="style">
        .wibble {font-variant: small-caps; font-weight: bold;}
      </style>
    </head>
    <body>
      <metal:block fill-slot="body">
        <p>I am a <span class="wibble">page,</span> honest.</p>
      </metal:block>
      <script type="text/javascript" metal:fill-slot="javascript"
              defer="true" src="/++resource++my.js"> </script>
    </body>
  </html>

The ``defer="true"`` is important: while both jQuery and Bootstrap are
loaded by default, the loading of both is deferred until *after* the page
has loaded. Anything that wants to use jQuery has to have ``defer="true"``
set.

.. [#page] See the ``gs.content.base`` product
           <http://github.com/groupserver/gs.content.base/>
