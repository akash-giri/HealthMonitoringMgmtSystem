$(function() {
    'use strict'
    $('[data-toggle="control-sidebar"]').controlSidebar()
    $('[data-toggle="push-menu"]').pushMenu()
    var $pushMenu = $('[data-toggle="push-menu"]').data('lte.pushmenu')
    var $controlSidebar = $('[data-toggle="control-sidebar"]').data('lte.controlsidebar')
    var $layout = $('body').data('lte.layout')
    $(window).on('load', function() {
        $pushMenu = $('[data-toggle="push-menu"]').data('lte.pushmenu')
        $controlSidebar = $('[data-toggle="control-sidebar"]').data('lte.controlsidebar')
        $layout = $('body').data('lte.layout')
    })
    var mySkins = ['skin-blue', 'skin-black', 'skin-red', 'skin-yellow', 'skin-purple', 'skin-green', 'skin-blue-light', 'skin-black-light', 'skin-red-light', 'skin-yellow-light', 'skin-purple-light', 'skin-green-light']

    function get(name) {
        if (typeof(Storage) !== 'undefined') {
            return localStorage.getItem(name)
        } else {
            window.alert('Please use a modern browser to properly view this template!')
        }
    }

    function store(name, val) {
        if (typeof(Storage) !== 'undefined') {
            localStorage.setItem(name, val)
        } else {
            window.alert('Please use a modern browser to properly view this template!')
        }
    }

    function changeLayout(cls) {
        $('body').toggleClass(cls)
        $layout.fixSidebar()
        if ($('body').hasClass('fixed') && cls == 'fixed') {
            $pushMenu.expandOnHover()
            $layout.activate()
        }
        $controlSidebar.fix()
    }

    function changeSkin(cls) {
        $.each(mySkins, function(i) {
            $('body').removeClass(mySkins[i])
        })
        $('body').addClass(cls)
        store('skin', cls)
        return false
    }

    function setup() {
        var tmp = get('skin')
        if (tmp && $.inArray(tmp, mySkins))
            changeSkin(tmp)
        $('[data-skin]').on('click', function(e) {
            if ($(this).hasClass('knob'))
                return
            e.preventDefault()
            changeSkin($(this).data('skin'))
        })
        $('[data-layout]').on('click', function() {
            changeLayout($(this).data('layout'))
        })
        $('[data-controlsidebar]').on('click', function() {
            changeLayout($(this).data('controlsidebar'))
            var slide = !$controlSidebar.options.slide
            $controlSidebar.options.slide = slide
            if (!slide)
                $('.control-sidebar').removeClass('control-sidebar-open')
        })
        $('[data-sidebarskin="toggle"]').on('click', function() {
            var $sidebar = $('.control-sidebar')
            if ($sidebar.hasClass('control-sidebar-dark')) {
                $sidebar.removeClass('control-sidebar-dark')
                $sidebar.addClass('control-sidebar-light')
            } else {
                $sidebar.removeClass('control-sidebar-light')
                $sidebar.addClass('control-sidebar-dark')
            }
        })
        $('[data-enable="expandOnHover"]').on('click', function() {
            $(this).attr('disabled', true)
            $pushMenu.expandOnHover()
            if (!$('body').hasClass('sidebar-collapse'))
                $('[data-layout="sidebar-collapse"]').click()
        })
        if ($('body').hasClass('fixed')) {
            $('[data-layout="fixed"]').attr('checked', 'checked')
        }
        if ($('body').hasClass('layout-boxed')) {
            $('[data-layout="layout-boxed"]').attr('checked', 'checked')
        }
        if ($('body').hasClass('sidebar-collapse')) {
            $('[data-layout="sidebar-collapse"]').attr('checked', 'checked')
        }
    }
    var $tabPane = $('<div />', {
        'id': 'control-sidebar-theme-demo-options-tab',
        'class': 'tab-pane active'
    })
    var $tabButton = $('<li />', {
        'class': 'active'
    }).html('<a href=\'#control-sidebar-theme-demo-options-tab\' data-toggle=\'tab\'>' +
        '<i class="fa fa-wrench"></i>' +
        '</a>')
    $('[href="#control-sidebar-home-tab"]').parent().before($tabButton)
    var $demoSettings = $('<div />')
    $demoSettings.append('<h4 class="control-sidebar-heading">' +
        'Layout Options' +
        '</h4>' +
        '<div class="form-group">' +
        '<label class="control-sidebar-subheading">' +
        '<input type="checkbox"data-layout="fixed"class="pull-right"/> ' +
        'Fixed layout' +
        '</label>' +
        '<p>Activate the fixed layout. You can\'t use fixed and boxed layouts together</p>' +
        '</div>' +
        '<div class="form-group">' +
        '<label class="control-sidebar-subheading">' +
        '<input type="checkbox"data-layout="layout-boxed" class="pull-right"/> ' +
        'Boxed Layout' +
        '</label>' +
        '<p>Activate the boxed layout</p>' +
        '</div>' +
        '<div class="form-group">' +
        '<label class="control-sidebar-subheading">' +
        '<input type="checkbox"data-layout="sidebar-collapse"class="pull-right"/> ' +
        'Toggle Sidebar' +
        '</label>' +
        '<p>Toggle the left sidebar\'s state (open or collapse)</p>' +
        '</div>' +
        '<div class="form-group">' +
        '<label class="control-sidebar-subheading">' +
        '<input type="checkbox"data-enable="expandOnHover"class="pull-right"/> ' +
        'Sidebar Expand on Hover' +
        '</label>' +
        '<p>Let the sidebar mini expand on hover</p>' +
        '</div>' +
        '<div class="form-group">' +
        '<label class="control-sidebar-subheading">' +
        '<input type="checkbox"data-controlsidebar="control-sidebar-open"class="pull-right"/> ' +
        'Toggle Right Sidebar Slide' +
        '</label>' +
        '<p>Toggle between slide over content and push content effects</p>' +
        '</div>' +
        '<div class="form-group">' +
        '<label class="control-sidebar-subheading">' +
        '<input type="checkbox"data-sidebarskin="toggle"class="pull-right"/> ' +
        'Toggle Right Sidebar Skin' +
        '</label>' +
        '<p>Toggle between dark and light skins for the right sidebar</p>' +
        '</div>')
    var $skinsList = $('<ul />', {
        'class': 'list-unstyled clearfix'
    })
    var $skinBlue = $('<li />', {
        style: 'float:left; width: 33.33333%; padding: 5px;'
    }).append('<a href="javascript:void(0)" data-skin="skin-blue" style="display: block; box-shadow: 0 0 3px rgba(0,0,0,0.4)" class="clearfix full-opacity-hover">' +
        '<div><span style="display:block; width: 20%; float: left; height: 7px; background: #367fa9"></span><span class="bg-light-blue" style="display:block; width: 80%; float: left; height: 7px;"></span></div>' +
        '<div><span style="display:block; width: 20%; float: left; height: 20px; background: #222d32"></span><span style="display:block; width: 80%; float: left; height: 20px; background: #f4f5f7"></span></div>' +
        '</a>' +
        '<p class="text-center no-margin">Blue</p>')
    $skinsList.append($skinBlue)
    var $skinBlack = $('<li />', {
        style: 'float:left; width: 33.33333%; padding: 5px;'
    }).append('<a href="javascript:void(0)" data-skin="skin-black" style="display: block; box-shadow: 0 0 3px rgba(0,0,0,0.4)" class="clearfix full-opacity-hover">' +
        '<div style="box-shadow: 0 0 2px rgba(0,0,0,0.1)" class="clearfix"><span style="display:block; width: 20%; float: left; height: 7px; background: #fefefe"></span><span style="display:block; width: 80%; float: left; height: 7px; background: #fefefe"></span></div>' +
        '<div><span style="display:block; width: 20%; float: left; height: 20px; background: #222"></span><span style="display:block; width: 80%; float: left; height: 20px; background: #f4f5f7"></span></div>' +
        '</a>' +
        '<p class="text-center no-margin">Black</p>')
    $skinsList.append($skinBlack)
    var $skinPurple = $('<li />', {
        style: 'float:left; width: 33.33333%; padding: 5px;'
    }).append('<a href="javascript:void(0)" data-skin="skin-purple" style="display: block; box-shadow: 0 0 3px rgba(0,0,0,0.4)" class="clearfix full-opacity-hover">' +
        '<div><span style="display:block; width: 20%; float: left; height: 7px;" class="bg-purple-active"></span><span class="bg-purple" style="display:block; width: 80%; float: left; height: 7px;"></span></div>' +
        '<div><span style="display:block; width: 20%; float: left; height: 20px; background: #222d32"></span><span style="display:block; width: 80%; float: left; height: 20px; background: #f4f5f7"></span></div>' +
        '</a>' +
        '<p class="text-center no-margin">Purple</p>')
    $skinsList.append($skinPurple)
    var $skinGreen = $('<li />', {
        style: 'float:left; width: 33.33333%; padding: 5px;'
    }).append('<a href="javascript:void(0)" data-skin="skin-green" style="display: block; box-shadow: 0 0 3px rgba(0,0,0,0.4)" class="clearfix full-opacity-hover">' +
        '<div><span style="display:block; width: 20%; float: left; height: 7px;" class="bg-green-active"></span><span class="bg-green" style="display:block; width: 80%; float: left; height: 7px;"></span></div>' +
        '<div><span style="display:block; width: 20%; float: left; height: 20px; background: #222d32"></span><span style="display:block; width: 80%; float: left; height: 20px; background: #f4f5f7"></span></div>' +
        '</a>' +
        '<p class="text-center no-margin">Green</p>')
    $skinsList.append($skinGreen)
    var $skinRed = $('<li />', {
        style: 'float:left; width: 33.33333%; padding: 5px;'
    }).append('<a href="javascript:void(0)" data-skin="skin-red" style="display: block; box-shadow: 0 0 3px rgba(0,0,0,0.4)" class="clearfix full-opacity-hover">' +
        '<div><span style="display:block; width: 20%; float: left; height: 7px;" class="bg-red-active"></span><span class="bg-red" style="display:block; width: 80%; float: left; height: 7px;"></span></div>' +
        '<div><span style="display:block; width: 20%; float: left; height: 20px; background: #222d32"></span><span style="display:block; width: 80%; float: left; height: 20px; background: #f4f5f7"></span></div>' +
        '</a>' +
        '<p class="text-center no-margin">Red</p>')
    $skinsList.append($skinRed)
    var $skinYellow = $('<li />', {
        style: 'float:left; width: 33.33333%; padding: 5px;'
    }).append('<a href="javascript:void(0)" data-skin="skin-yellow" style="display: block; box-shadow: 0 0 3px rgba(0,0,0,0.4)" class="clearfix full-opacity-hover">' +
        '<div><span style="display:block; width: 20%; float: left; height: 7px;" class="bg-yellow-active"></span><span class="bg-yellow" style="display:block; width: 80%; float: left; height: 7px;"></span></div>' +
        '<div><span style="display:block; width: 20%; float: left; height: 20px; background: #222d32"></span><span style="display:block; width: 80%; float: left; height: 20px; background: #f4f5f7"></span></div>' +
        '</a>' +
        '<p class="text-center no-margin">Yellow</p>')
    $skinsList.append($skinYellow)
    var $skinBlueLight = $('<li />', {
        style: 'float:left; width: 33.33333%; padding: 5px;'
    }).append('<a href="javascript:void(0)" data-skin="skin-blue-light" style="display: block; box-shadow: 0 0 3px rgba(0,0,0,0.4)" class="clearfix full-opacity-hover">' +
        '<div><span style="display:block; width: 20%; float: left; height: 7px; background: #367fa9"></span><span class="bg-light-blue" style="display:block; width: 80%; float: left; height: 7px;"></span></div>' +
        '<div><span style="display:block; width: 20%; float: left; height: 20px; background: #f9fafc"></span><span style="display:block; width: 80%; float: left; height: 20px; background: #f4f5f7"></span></div>' +
        '</a>' +
        '<p class="text-center no-margin" style="font-size: 12px">Blue Light</p>')
    $skinsList.append($skinBlueLight)
    var $skinBlackLight = $('<li />', {
        style: 'float:left; width: 33.33333%; padding: 5px;'
    }).append('<a href="javascript:void(0)" data-skin="skin-black-light" style="display: block; box-shadow: 0 0 3px rgba(0,0,0,0.4)" class="clearfix full-opacity-hover">' +
        '<div style="box-shadow: 0 0 2px rgba(0,0,0,0.1)" class="clearfix"><span style="display:block; width: 20%; float: left; height: 7px; background: #fefefe"></span><span style="display:block; width: 80%; float: left; height: 7px; background: #fefefe"></span></div>' +
        '<div><span style="display:block; width: 20%; float: left; height: 20px; background: #f9fafc"></span><span style="display:block; width: 80%; float: left; height: 20px; background: #f4f5f7"></span></div>' +
        '</a>' +
        '<p class="text-center no-margin" style="font-size: 12px">Black Light</p>')
    $skinsList.append($skinBlackLight)
    var $skinPurpleLight = $('<li />', {
        style: 'float:left; width: 33.33333%; padding: 5px;'
    }).append('<a href="javascript:void(0)" data-skin="skin-purple-light" style="display: block; box-shadow: 0 0 3px rgba(0,0,0,0.4)" class="clearfix full-opacity-hover">' +
        '<div><span style="display:block; width: 20%; float: left; height: 7px;" class="bg-purple-active"></span><span class="bg-purple" style="display:block; width: 80%; float: left; height: 7px;"></span></div>' +
        '<div><span style="display:block; width: 20%; float: left; height: 20px; background: #f9fafc"></span><span style="display:block; width: 80%; float: left; height: 20px; background: #f4f5f7"></span></div>' +
        '</a>' +
        '<p class="text-center no-margin" style="font-size: 12px">Purple Light</p>')
    $skinsList.append($skinPurpleLight)
    var $skinGreenLight = $('<li />', {
        style: 'float:left; width: 33.33333%; padding: 5px;'
    }).append('<a href="javascript:void(0)" data-skin="skin-green-light" style="display: block; box-shadow: 0 0 3px rgba(0,0,0,0.4)" class="clearfix full-opacity-hover">' +
        '<div><span style="display:block; width: 20%; float: left; height: 7px;" class="bg-green-active"></span><span class="bg-green" style="display:block; width: 80%; float: left; height: 7px;"></span></div>' +
        '<div><span style="display:block; width: 20%; float: left; height: 20px; background: #f9fafc"></span><span style="display:block; width: 80%; float: left; height: 20px; background: #f4f5f7"></span></div>' +
        '</a>' +
        '<p class="text-center no-margin" style="font-size: 12px">Green Light</p>')
    $skinsList.append($skinGreenLight)
    var $skinRedLight = $('<li />', {
        style: 'float:left; width: 33.33333%; padding: 5px;'
    }).append('<a href="javascript:void(0)" data-skin="skin-red-light" style="display: block; box-shadow: 0 0 3px rgba(0,0,0,0.4)" class="clearfix full-opacity-hover">' +
        '<div><span style="display:block; width: 20%; float: left; height: 7px;" class="bg-red-active"></span><span class="bg-red" style="display:block; width: 80%; float: left; height: 7px;"></span></div>' +
        '<div><span style="display:block; width: 20%; float: left; height: 20px; background: #f9fafc"></span><span style="display:block; width: 80%; float: left; height: 20px; background: #f4f5f7"></span></div>' +
        '</a>' +
        '<p class="text-center no-margin" style="font-size: 12px">Red Light</p>')
    $skinsList.append($skinRedLight)
    var $skinYellowLight = $('<li />', {
        style: 'float:left; width: 33.33333%; padding: 5px;'
    }).append('<a href="javascript:void(0)" data-skin="skin-yellow-light" style="display: block; box-shadow: 0 0 3px rgba(0,0,0,0.4)" class="clearfix full-opacity-hover">' +
        '<div><span style="display:block; width: 20%; float: left; height: 7px;" class="bg-yellow-active"></span><span class="bg-yellow" style="display:block; width: 80%; float: left; height: 7px;"></span></div>' +
        '<div><span style="display:block; width: 20%; float: left; height: 20px; background: #f9fafc"></span><span style="display:block; width: 80%; float: left; height: 20px; background: #f4f5f7"></span></div>' +
        '</a>' +
        '<p class="text-center no-margin" style="font-size: 12px">Yellow Light</p>')
    $skinsList.append($skinYellowLight)
    $demoSettings.append('<h4 class="control-sidebar-heading">Skins</h4>')
    $demoSettings.append($skinsList)
    $tabPane.append($demoSettings)
    $('#control-sidebar-home-tab').after($tabPane)
    setup()
    $('[data-toggle="tooltip"]').tooltip()
})