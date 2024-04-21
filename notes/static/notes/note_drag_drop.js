$(document).ready(function() {
    console.log('sortable init')
//    TODO: this ajax call is not being triggered
    new Sortable(noteList, {
        animation: 150,
        ghostClass: 'sortable-ghost',
        update: function(event, ui) {
            // Update the order of notes in the database using AJAX
            var noteIds = $(this).sortable('serialize');
            console.log('ajax call')
            $.ajax({
                url: '{% url "notes.reorder" %}',
                method: 'post',
                data: { order: noteIds },
                headers: { 'X-CSRFToken': '{{ csrf_token }}' },
            });
        }
    });
})