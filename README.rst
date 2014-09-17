=====================
``gs.content.layout``
=====================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The core page layout for GroupServer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Authors: `Michael JasonSmith`_,
         Richard Waid
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2014-09-17
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

Introduction
============

This egg defines the standard `layouts`_ for pages on GroupServer_.  The
layouts provide `slots`_ that are filled by the pages that provide the
content. By using these standard layouts less code is required to get all
the pages to look consistent.

Layouts
=======

There are two standard `layouts`_ for pages on GroupServer_:

* A `full-page layout`_, and
* A `layout with a menu`_.

Full-Page Layout
----------------

The full-page layout is the standard layout for GroupServer. To use the
full-page layout with your page first add a ``metal:use-macro`` call to the
``<html>`` element::

  <html xmlns="http://www.w3.org/1999/xhtml"
    xmlns:tal="http://xml.zope.org/namespaces/tal"
    xmlns:metal="http://xml.zope.org/namespaces/metal"
    metal:use-macro="context/@@groupserver_full_layout/page">

Then fill the `slots`_.

Layout with a Menu
------------------

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
  slot appears after the standard GroupServer CSS [#css]_, so the page can
  overwrite the general style.

``metal:fill-slot="utilitylinks"``:
  The optional *utility* menu. The only time this is ever set is to ensure
  the is *no* menu. By default the utility links show either:
  
  * A *Login* link, or
  * A *Log Out* link and a *Profile* link.

``metal:fill-slot="breadcrumb"``:
  The optional *breadcrumb trail*. It is normally an unordered list, with
  the first item a link to the site-homepage::
    
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
  content-provider supplied by the ``gs.content.form`` egg [#form]_::

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

Examples
========

Below are some examples for using the pay layouts.

A Simple Page
-------------

*Most* pages only have to fill three slots: the ``title``, ``breadcrumb``
and the ``body``::

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
          <a tal:attributes="title string:${view/siteInfo/name} Homepage"
             href="/" title="Home">&#8962;</a>
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
slot and the rest of the page::

    <head>
      <title metal:fill-slot="title">I am a page: 
        <span tal:replace="view/siteInfo/name">wibble</span></title>
    </head>

The ``tal:replace`` attribute is used because a ``<span>`` element is not
actually allowed to appear within a ``<title>``. A ``<tal:block>`` could
also be used.

Page-Specific Style and JavaScript
----------------------------------

Some pages have some page-specific CSS styling and JavaScript::

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

Resources
=========

- Code repository: https://github.com/groupserver/gs.content.layout
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net/
.. _Michael JasonSmith: http://groupserver.org/p/mpj17/

.. [#css] See the ``gs.content.css`` product
          <http://github.com/groupserver/gs.content.css/>

.. [#form] See the ``gs.content.form`` product
           <http://github.com/groupserver/gs.content.form/>

.. [#jquery] See the ``gs.content.js.jquery`` product
           <http://github.com/groupserver/gs.content.js.jquery/>

.. [#page] See the ``gs.content.base`` product
           <http://github.com/groupserver/gs.content.base/>
