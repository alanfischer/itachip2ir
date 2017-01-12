#ifndef ITACHIP2IR_H
#define ITACHIP2IR_H

#include <string>
#include "IRCommand.h"

class ITachIP2IR{
public:
	ITachIP2IR(std::string mac,std::string ip,int port);
    ~ITachIP2IR();

	bool ready() const{return dataSocket!=-1;}

	bool send(int modaddr,int connaddr,IRCommand *command,int count);

	void update();

	static std::string commandToGC(int modaddr,int connaddr,IRCommand *command,int count);

protected:
	int parseResponse(char *message);
	bool parseBroadcast(char *message,std::string &mac,std::string &ip);
	int tryResponse(int timeout);
	void tryPing();
	void tryBeacon();
	void tryConnect();

    std::string macAddress,ipAddress;
	int port;
	int beaconSocket,connectingSocket,dataSocket;
};

#endif
