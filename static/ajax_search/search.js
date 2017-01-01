$(function(){
	$('.search').on('keyup', function() {
		$.ajax({
			url: '/search/',
			type: 'POST',
			data: {
				search:$('.search').val(),
				csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
			},
			success:function(data) {
				$('#search-list').html(data);
			}
		});
	});
});

