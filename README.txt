Introduction
============

This egg defines the two standard *layouts* for pages on GroupServer_:

* A `full-page layout`_, and
* A `layout with a menu`_.

Both provide the equivalent `slots`_. By using these standard layouts less
code is required to get all the pages to look consistent.

Full-Page Layout
================

The full-page layout is the standard layout for GroupServer. To use the
full-page layout with your page first add a ``metal:use-macro`` call to the
``<html>`` element::

  <html xmlns="http://www.w3.org/1999/xhtml"
    xmlns:tal="http://xml.zope.org/namespaces/tal"
    xmlns:metal="http://xml.zope.org/namespaces/metal"
    metal:use-macro="context/@@groupserver_full_layout/page">

Then fill the `slots`_.

Layout with a Menu
==================

The layout with a menu has a *context menu* running down the left-hand side
of the page. Otherwise it is exactly the same as the `full-page
layout`_. To use the layout with a menu use the ``groupserver_menu_layout``
macro::

  <html xmlns="http://www.w3.org/1999/xhtml"
    xmlns:tal="http://xml.zope.org/namespaces/tal"
    xmlns:metal="http://xml.zope.org/namespaces/metal"
    metal:use-macro="context/@@groupserver_menu_layout/page">

Then fill the `slots`_.

Slots
=====

There are nine slots defined by the two layouts. 

``metal:fill-slot="title"``:
  The compulsory title of the page. It is **always** provided by pages that
  use the standard layouts, and **always** contains a ``<title>`` element::
  
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
  slot appears after the standard GroupServer CSS, so the page can
  overwrite the general style.

``metal:fill-slot="sitenavigation"``:
  The optional *site-navigation menu* (also known as the *main menu*). A
  default menu will be provided if the page does not fill this slot. Almost
  the only time this is ever set is to ensure there is *no* menu::

    <metal:block fill-slot="sitenavigation">&#160;</metal:block>

``metal:fill-slot="utilitylinks"``:
  The optional *utility* menu. The only time this is ever set is to ensure
  the is *no* menu. By default the utility links show either:
  
  * A *Login* link, or
  * A *Log Out* link and a *Profile* link.

``metal:fill-slot="messages"``:
  Feedback messages for the form. This is almost only ever filled by the
  content-provider supplied by the ``gs.content.form`` egg::

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
  page-specific scripts appear *after* the standard JQuery code has been
  loaded, and the rest of the page has been rendered.

Examples
--------

*Most* pages only have to fill two: the ``title`` and the ``body``::

  <html xmlns="http://www.w3.org/1999/xhtml"
    xmlns:tal="http://xml.zope.org/namespaces/tal"
    xmlns:metal="http://xml.zope.org/namespaces/metal"
    metal:use-macro="context/@@groupserver_full_layout/page">
    <head>
      <title metal:fill-slot="title">I am a page: Example</title>
    </head>
    <body metal:fill-slot="body">
      <p>I am a page, honest.</p>
    </body>
  </html>

The rest of the slots will be filled by the defaults.

Some pages have some page-specific CSS styling and JavaScript::

  <html xmlns="http://www.w3.org/1999/xhtml"
    xmlns:tal="http://xml.zope.org/namespaces/tal"
    xmlns:metal="http://xml.zope.org/namespaces/metal"
    metal:use-macro="context/@@groupserver_full_layout/page">
    <head>
      <title metal:fill-slot="title">I am a page: Example</title>
      <style type="text/css" metal:fill-slot="style">
        .wibble {font-variant: small-caps; font-weight: bold;}
    </head>
    <body>
      <metal:block fill-slot="body">
        <p>I am a <span class="wibble">page,</span> honest.</p>
      </metal:block>
      <script type="text/javascript" metal:fill-slot="javascript">
        jQuery(document).ready( function () {
           alert('ZOMG Pages!');
        });
      </script>
    </body>
  </html>


.. _GroupServer: http://groupserver.org/
.. _OnlineGroups.Net: http://onlinegroups.net/

