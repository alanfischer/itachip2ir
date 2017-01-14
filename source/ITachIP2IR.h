#ifndef ITACHIP2IR_H
#define ITACHIP2IR_H

#include <string>
#include <vector>
#include "IRCommand.h"

class ITachIP2IR{
public:
	ITachIP2IR(std::string mac,std::string ip,int port);
	~ITachIP2IR();

	bool ready(int timeout){return dataSocket!=-1 || checkConnect(timeout);}

	bool loadCommands(char *text);

	bool send(int modaddr,int connaddr,IRCommand *command,int count);
	bool send(int modaddr,int connaddr,std::string command,int count);

	void update();

protected:
	int parseResponse(char *message);
	bool parseBroadcast(char *message,std::string &mac,std::string &ip);
	int tryResponse(int timeout);
	void tryPing();
	void tryBeacon();
	void tryConnect();
	bool checkConnect(int timeout);
	static std::string commandToGC(int modaddr,int connaddr,IRCommand *command,int count);

	std::string macAddress,ipAddress;
	int port;
	int beaconSocket,connectingSocket,dataSocket;
	std::vector<IRCommand> commands;
};

#endif
