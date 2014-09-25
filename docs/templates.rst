:mod:`gs.content.form.base` Templates
=====================================

Layouts
-------


There are two standard `layouts`_ for pages on GroupServer_:

* A `full-page layout`_, and
* A `layout with a menu`_.

Full-Page Layout
----------------

The full-page layout is the standard layout for GroupServer. To
use the full-page layout with your page first add a
``metal:use-macro`` call to the ``<html>`` element.

.. code-block:: xml

  <html xmlns="http://www.w3.org/1999/xhtml"
        xmlns:tal="http://xml.zope.org/namespaces/tal"
        xmlns:metal="http://xml.zope.org/namespaces/metal"
        metal:use-macro="context/@@groupserver_full_layout/page">

Then fill the `slots`_.

Layout with a Menu
------------------

The layout with a menu has a *context menu* running down the
left-hand side of the page. Otherwise it is exactly the same as
the `full-page layout`_. To use the layout with a menu use the
``groupserver_menu_layout`` macro.

.. code-block:: xml

  <html xmlns="http://www.w3.org/1999/xhtml"
        xmlns:tal="http://xml.zope.org/namespaces/tal"
        xmlns:metal="http://xml.zope.org/namespaces/metal"
        metal:use-macro="context/@@groupserver_menu_layout/page">

Then fill the `slots`_.

Slots
-----


There are nine slots defined by the two layouts. 

``metal:fill-slot="title"``:
  The compulsory title of the page. It is **always** provided by pages that
  use the standard layouts, and **always** contains a ``<title>`` element.
  
.. code-block:: xml

    <title metal:fill-slot="title">This is the title</title>

``metal:fill-slot="metadata"``:
  Optional extra metadata for the page. While ``<meta>`` elements can be
  added they almost never are. However, ``<link>`` elements are often added
  (especially in pages that would use a breadcrumb trail, such as within
  groups). Normally a ``<metal:block>`` element has the ``fill-slot``
  attribute, and the metadata to add is placed inside the block.

``metal:fill-slot="style"``:
  Optional extra style (CSS) information for the page. Normally a
  ``<style>`` element has the ``fill-slot`` macro. When rendered the style
  slot appears after the standard GroupServer CSS [#css]_, so the page can
  overwrite the general style.

``metal:fill-slot="utilitylinks"``:
  The optional *utility* menu. The only time this is ever set is to ensure
  the is *no* menu. By default the utility links show either:
  
  * A *Login* link, or
  * A *Log Out* link and a *Profile* link.

``metal:fill-slot="breadcrumb"``:
  The optional *breadcrumb trail*. It is normally an unordered list, with
  the first item a link to the site-homepage.
    
.. code-block:: xml

   <ul metal:fill-slot="breadcrumb">
     <li>
        <a href="/" class="icon-alone">
          <span aria-hidden="true" data-icon="&#x2302;"></span>
          <span class="screen-reader-text">Site home page</span>
        </a>
     </li>
     <li>
       <a href="#"><strong>Important</strong></a>
     </li>
     <li>
       A page.
     </li>
   </ul>

``metal:fill-slot="messages"``:
  Feedback messages for the form. This is almost only ever filled by the
  content-provider supplied by the ``gs.content.form`` egg [#form]_.

.. code-block:: xml

    <tal:block
      content="structure provider:groupserver.FormStatusMessage"
      define="errors view/errors; status view/status; widgets view/widgets"
      metal:fill-slot="messages">&#160;</tal:block>

``metal:fill-slot="body"``:
  The **compulsory** body of the page.

``metal:fill-slot="footer"``:
  The optional footer of the page. It appears after the body. By default it
  contains the contents of the ``Templates/output/footerlinks.xml``
  instance in the ZMI.

``metal:fill-slot="javascript"``:
  The JavaScript (technically the ECMAScript) for the page. The
  page-specific scripts appear *after* the standard JQuery code [#jquery]_
  has been loaded, and the rest of the page has been rendered.

.. _GroupServer: http://groupserver.org/

.. [#css] See the ``gs.content.css`` product
          <http://github.com/groupserver/gs.content.css/>

.. [#form] See the ``gs.content.form`` product
           <http://github.com/groupserver/gs.content.form/>

.. [#jquery] See the ``gs.content.js.jquery`` product
           <http://github.com/groupserver/gs.content.js.jquery/>

