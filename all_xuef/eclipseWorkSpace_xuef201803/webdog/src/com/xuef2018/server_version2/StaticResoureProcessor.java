package com.xuef2018.server_version2;

import java.io.IOException;

public class StaticResoureProcessor {

	public void process(Request1 request, Response1 response) 
			throws IOException {
		response.sendStaticResource();
	}

}
