#include "crow.h"
#include "cpp_redis/core/client.hpp"
#include "string"

#include <iostream>
#include <vector>
#include <utility>
//#include "crow_all.h"

using namespace crow;
using namespace std;



int main()
{
    SimpleApp app;

    cpp_redis::client redisClient;
    redisClient.connect();

    CROW_ROUTE(app, "/health")([](){
        return "Working fine...";
    });

    CROW_ROUTE(app, "/api/blogs").methods(HTTPMethod::POST)
    ([&](const request& req)
    {
        auto body = json::load(req.body);
        if (!body)
            return response(400, "Invalid body");
        
        string title, content;
        
        try {
            title = body["title"].s();
            content = body["content"].s();
        } catch (const runtime_error &err) {
            return response(400, "Invalid body");
        }

        try {
            redisClient.lpush("titles", { title });
            redisClient.lpush("contents", { content });
            redisClient.sync_commit();
        } catch (const runtime_error &ex) {
            return response(500, "Internal Server Error");
        }

        return response(200, "Blog added");
    });

    CROW_ROUTE(app, "/api/blogs")
    ([&]()
    {
        auto r1 = redisClient.lrange("titles", 0, -1);
        auto r2 = redisClient.lrange("contents", 0, -1);
        redisClient.sync_commit();
        r1.wait();
        r2.wait();
        auto r = r1.get().as_array();
        vector<string> titles(r.size()), contents(r.size());
        transform(r.begin(), r.end(), titles.begin(), [](const cpp_redis::reply &rep) { return rep.as_string(); });

        auto rC = r2.get().as_array();
        transform(rC.begin(), rC.end(), contents.begin(), [](const cpp_redis::reply &rep) { return rep.as_string(); });

        vector<json::wvalue> blogs;
        for (int i = 0; i < titles.size(); i++){
            blogs.push_back(
                json::wvalue{
                    {"title", titles[i]},
                    {"content", contents[i]}
                }
                
            );
        }

        return json::wvalue{{"data", blogs}};
    });

    app.port(3000).multithreaded().run();
}
