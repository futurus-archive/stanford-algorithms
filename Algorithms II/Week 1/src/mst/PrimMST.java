package mst;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

/**
 * Created by vunguyen on 1/16/17.
 */

class Vertex {
    private int id;
    private HashMap<Vertex, Integer> edges;

    public Vertex(int vid) {
        id = vid;
        edges = new HashMap<Vertex, Integer>();
    }

    public int getId() {
        return id;
    }

    public int nEdges() {
        return edges.size();
    }

    public void connect(Vertex to, Integer weight) {
        edges.put(to, weight);
    }
}

class Graph {
    private ArrayList<Vertex> vertices;

    public Graph() {
        vertices = new ArrayList<Vertex>();
    }

    public int nVertices() {
        return vertices.size();
    }

    public boolean containsVertex(int id) {
        for (Vertex vertex : vertices) {
            if (vertex.getId() == id) {
                return true;
            }
        }

        return false;
    }

    public boolean containsVertex(Vertex v) {
        return vertices.contains(v);
    }

    public void addVertex(Vertex v) {
        vertices.add(v);
    }

    public Vertex getVertex(int id) {
        for (Vertex vertex : vertices) {
            if (vertex.getId() == id) {
                return vertex;
            }
        }

        return null;
    }

    public ArrayList<Vertex> getVertices() {
        return vertices;
    }

    public boolean removeVertex(Vertex v) {
        if (vertices.contains(v)) {
            vertices.remove(v);
            return true;
        }
        return false;
    }
}

public class PrimMST {
    public static Graph getGraph(String filename) throws IOException {
        File file = new File(filename); //for ex foo.txt
        Scanner sc = null;
        Graph g = null;

        try {
            sc = new Scanner(file);
            int nNodes = sc.nextInt();
            int nEdges = sc.nextInt();
            g = new Graph();

            System.out.println(nNodes + " --- " + nEdges);

            for (int i = 0; i < nEdges; i++) {
                int f = sc.nextInt();
                int t = sc.nextInt();
                int w = sc.nextInt();

                if (g.containsVertex(f)) {
                    if (g.containsVertex(t)) {
                        g.getVertex(f).connect(g.getVertex(t), w);
                    } else {
                        g.addVertex(new Vertex(t));
                        g.getVertex(f).connect(g.getVertex(t), w);
                    }
                    g.getVertex(t).connect(g.getVertex(f), w);
                } else {
                    Vertex v = new Vertex(f);
                    g.addVertex(v);

                    if (g.containsVertex(t)) {
                        g.getVertex(f).connect(g.getVertex(t), w);
                    } else {
                        g.addVertex(new Vertex(t));
                        g.getVertex(f).connect(g.getVertex(t), w);
                    }
                }
                g.getVertex(t).connect(g.getVertex(f), w);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (sc != null) {
                sc.close();
            }
            return g;
        }
    }

    public static void main(String[] args) {
        try {
            Graph g = getGraph("data/edges.txt");
            Graph t = new Graph();

        } catch (IOException e) {
        }
    }
}
