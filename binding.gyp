{
	"targets": [
		{
			"target_name": "protobuf_for_node",
			"include_dirs": ["<!(node -e \"require('nan')\")", "protobuf/src"],
			"dependencies": ["protobuf/protobuf.gyp:protobuf_full_do_not_use"],
			"sources": [
				"protobuf_for_node.cc", "addon.cc"
			],
			'conditions': [
				[
					'OS =="mac"',{
						'xcode_settings':{
						  'OTHER_CFLAGS' : [
							'-mmacosx-version-min=10.7'
						  ]
						}
			  		}
				]
			]
		}
	]
}
