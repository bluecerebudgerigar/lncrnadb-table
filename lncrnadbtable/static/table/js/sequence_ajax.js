/* library files to allow ajax calling to get details of sequences */




$(function(){
    function bindDumpButton() {
        $('body').on('click', 'button[name=dump]', function () {
            var dump = $(this).data('dump');
            var $container = $(dump);
            console.log('data of ' + dump, $container.handsontable('getData'));
        });
    }
    bindDumpButton();



})